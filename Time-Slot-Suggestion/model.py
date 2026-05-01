from sample_data import appointments # type: ignore
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sample_data import dentists, services # type: ignore


# Data Load
dentists_df = pd.DataFrame(dentists)
services_df = pd.DataFrame(services)

# Feature Engineering

# Services encode
mlb = MultiLabelBinarizer()
service_encoded = mlb.fit_transform(dentists_df['services'])

# Experience normalize 
scaler = MinMaxScaler()
experience_scaled = scaler.fit_transform(
    dentists_df[['experience']]
)

# Feature Matrix
feature_matrix = np.hstack([
    service_encoded,
    experience_scaled
])

feature_df = pd.DataFrame(
    feature_matrix,
    columns=list(mlb.classes_) + ['experience_scaled']
)
feature_df['dentist_id'] = dentists_df['dentist_id']
feature_df['name'] = dentists_df['name']


# Recommend Function
def recommend_dentist(service_name: str, top_n: int = 3):

    # Check service valid 
    all_services = services_df['name'].tolist()
    if service_name not in all_services:
        return {
            "message": f"Service not found! Available: {all_services}",
            "recommendations": []
        }

    # Service provide to dentists 
    matching = dentists_df[
        dentists_df['services'].apply(
            lambda x: service_name in x
        )
    ]

    if matching.empty:
        return {
            "message": "No dentist found for this service",
            "recommendations": []
        }

    # Feature matrix filter
    matching_ids = matching['dentist_id'].values
    matching_features = feature_df[
        feature_df['dentist_id'].isin(matching_ids)
    ]

    # Feature cols
    feature_cols = [
        col for col in feature_df.columns
        if col not in ['dentist_id', 'name']
    ]
    features = matching_features[feature_cols].values

    # Similarity
    similarity = cosine_similarity(features)
    first_sim = similarity[0]

    similar = sorted(
        enumerate(first_sim),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]

    # Result  
    recommendations = []
    for idx, score in similar:
        dentist = matching_features.iloc[idx]
        dentist_info = dentists_df[dentists_df['dentist_id'] == dentist['dentist_id']].iloc[0]

        # Service price
        service_info = services_df[services_df['name'] == service_name].iloc[0]

        recommendations.append({
            "dentist_id": int(dentist['dentist_id']),
            "name": dentist_info['name'],
            "specialty": dentist_info['specialty'],
            "experience": f"{dentist_info['experience']} years",
            "availableDays": dentist_info['availableDays'],
            "availableTime": dentist_info['availableTime'],
            "service": service_name,
            "price": int(service_info['price']),
            "duration": service_info['duration'],
            "match_score": round(float(score), 2)
        })

    return {
        "service": service_name,
        "recommendations": recommendations
    }


appointments_df = pd.DataFrame(appointments)

def get_available_slots(dentist_id: int, date: str):

    # Dentist exist 
    dentist = dentists_df[
        dentists_df['dentist_id'] == dentist_id
    ]

    if dentist.empty:
        return {
            "message": "Dentist not found!",
            "available_slots": []
        }

    dentist = dentist.iloc[0]

    # available on that day
    from datetime import datetime
    day_name = datetime.strptime(
        date, "%Y-%m-%d"
    ).strftime("%A")

    if day_name not in dentist['availableDays']:
        return {
            "message": f"Dr. {dentist['name']} is not available on {day_name}",
            "available_slots": []
        }

    #  All possible slots
    all_slots = [
        "9:00 AM", "10:00 AM", "11:00 AM",
        "12:00 PM", "2:00 PM", "3:00 PM",
        "4:00 PM", "5:00 PM"
    ]

    # Booked slots on that day
    booked_slots = appointments_df[
        (appointments_df['dentistId'] == dentist_id) &
        (appointments_df['date'] == date) &
        (appointments_df['status'] != 'cancelled')
    ]['time'].tolist()

    # Standalone Free slots
    free_slots = [
        slot for slot in all_slots
        if slot not in booked_slots
    ]

    return {
        "dentist_id": dentist_id,
        "dentist_name": dentist['name'],
        "date": date,
        "day": day_name,
        "booked_slots": booked_slots,
        "available_slots": free_slots,
        "total_available": len(free_slots)
    }