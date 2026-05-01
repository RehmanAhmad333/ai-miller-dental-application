from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Connection
uri = os.getenv("MONGO_URI")

try:
    client = MongoClient(uri, tlsCAFile=certifi.where())
    client.admin.command('ping')
    print("MongoDB connected successfully")
    db = client["test"]
except Exception as e:
    print("Connection failed:", e)
    db = None


# Load data from MongoDB
def load_data():
    if db is None:
        return None, None, None, None

    # Load dentists
    dentists_data = list(db.dentists.find({}, {"_id": 1, "name": 1, "specialty": 1, "experience": 1, "availableDays": 1,"availableTime": 1}))
    for d in dentists_data:
        d['dentist_id'] = str(d['_id'])
        del d['_id']

    # Load services
    services_data = list(db.services.find({}, {"_id": 1, "serviceName": 1,"price": 1, "duration": 1, "description": 1}))
    for s in services_data:
        s['service_id'] = str(s['_id'])
        s['name'] = s.get('serviceName', '')
        del s['_id']

    # Load appointments
    appointments_data = list(db.appointments.find({}, {"_id": 0, "userId": 1,"dentistId": 1, "serviceId": 1,"date": 1, "time": 1, "status": 1}))
    for a in appointments_data:
        a['userId'] = str(a.get('userId', ''))
        a['dentistId'] = str(a.get('dentistId', ''))
        a['serviceId'] = str(a.get('serviceId', ''))

    # Load users
    users_data = list(db.users.find({}, {"_id": 1, "name": 1, "email": 1}))
    for u in users_data:
        u['user_id'] = str(u['_id'])
        del u['_id']

    return (
        pd.DataFrame(dentists_data),
        pd.DataFrame(services_data),
        pd.DataFrame(appointments_data),
        pd.DataFrame(users_data)
    )


dentists_df, services_df, appointments_df, users_df = load_data()


# Build feature matrix for dentists
def build_feature_matrix(dentists_df, services_df):

    # Add services list to each dentist based on specialty
    service_names = services_df['name'].tolist()

    def match_services(specialty):
        matched = []
        specialty_lower = str(specialty).lower()
        for sname in service_names:
            if (sname.lower() in specialty_lower or
                    specialty_lower in sname.lower()):
                matched.append(sname)
        if not matched:
            matched = [service_names[0]]
        return matched

    dentists_df['matched_services'] = dentists_df['specialty'].apply(
        match_services
    )

    # Encode matched services
    mlb = MultiLabelBinarizer()
    service_encoded = mlb.fit_transform(dentists_df['matched_services'])

    # Normalize experience
    scaler = MinMaxScaler()

    # Handle experience field - convert to numeric
    dentists_df['exp_numeric'] = pd.to_numeric(
        dentists_df['experience'].astype(str).str.extract('(\d+)')[0],
        errors='coerce'
    ).fillna(0)

    experience_scaled = scaler.fit_transform(dentists_df[['exp_numeric']])

    # Build final feature matrix
    feature_matrix = np.hstack([service_encoded, experience_scaled])

    feature_df = pd.DataFrame(
        feature_matrix,
        columns=list(mlb.classes_) + ['experience_scaled']
    )
    feature_df['dentist_id'] = dentists_df['dentist_id'].values
    feature_df['name'] = dentists_df['name'].values

    return feature_df, mlb


if dentists_df is not None and services_df is not None:
    feature_df, mlb = build_feature_matrix(dentists_df, services_df)
else:
    feature_df = None
    mlb = None


# Recommend best dentist for a given service
def recommend_dentist(service_name: str, top_n: int = 3):

    if dentists_df is None or services_df is None:
        return {"message": "Database not connected", "recommendations": []}

    # Check service exists
    all_services = services_df['name'].tolist()
    if service_name not in all_services:
        return {
            "message": "Service not found",
            "available_services": all_services,
            "recommendations": []
        }

    # Get service info
    service_info = services_df[
        services_df['name'] == service_name
    ].iloc[0]

    # Find matching dentists
    matching = dentists_df[
        dentists_df['matched_services'].apply(
            lambda x: service_name in x
        )
    ]

    if matching.empty:
        matching = dentists_df.copy()

    matching_ids = matching['dentist_id'].values
    matching_features = feature_df[
        feature_df['dentist_id'].isin(matching_ids)
    ]

    if matching_features.empty:
        return {"message": "No dentist found", "recommendations": []}

    feature_cols = [
        col for col in feature_df.columns
        if col not in ['dentist_id', 'name']
    ]
    features = matching_features[feature_cols].values

    # Fix — sirf 1 dentist hai to similarity skip karo
    if len(features) == 1:
        scores = [1.0]
        indices = [0]
    else:
        similarity = cosine_similarity(features)
        first_sim = similarity[0]
        
        # Fix — NaN aur inf values replace karo
        first_sim = np.nan_to_num(
            first_sim, 
            nan=0.0, 
            posinf=1.0, 
            neginf=0.0
        )

        similar = sorted(
            enumerate(first_sim),
            key=lambda x: x[1],
            reverse=True
        )[:top_n]

        indices = [i for i, s in similar]
        scores = [s for i, s in similar]

    # Build response
    recommendations = []
    for pos, idx in enumerate(indices):
        dentist_row = matching_features.iloc[idx]
        dentist_info = dentists_df[
            dentists_df['dentist_id'] == dentist_row['dentist_id']
        ].iloc[0]

        # Convert score safely
        score = scores[pos]
        if np.isnan(score) or np.isinf(score):
            score = 0.0

        recommendations.append({
            "dentist_id": str(dentist_info['dentist_id']),
            "name": str(dentist_info['name']),
            "specialty": str(dentist_info['specialty']),
            "experience": str(dentist_info['experience']),
            "availableDays": dentist_info['availableDays'],
            "availableTime": str(dentist_info['availableTime']),
            "service": service_name,
            "price": int(service_info['price']),
            "duration": str(service_info['duration']),
            "match_score": round(float(score), 2)
        })

    return {
        "service": service_name,
        "total_recommendations": len(recommendations),
        "recommendations": recommendations
    }

# Get available time slots for a dentist on a given date
def get_available_slots(dentist_id: str, date: str):

    if dentists_df is None:
        return {"message": "Database not connected", "available_slots": []}

    # Find dentist
    dentist = dentists_df[dentists_df['dentist_id'] == dentist_id]

    if dentist.empty:
        return {"message": "Dentist not found", "available_slots": []}

    dentist = dentist.iloc[0]

    # Check if dentist works on that day
    try:
        day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    except ValueError:
        return {"message": "Invalid date format. Use YYYY-MM-DD", "available_slots": []}

    available_days = dentist['availableDays']
    if isinstance(available_days, list):
        if day_name not in available_days:
            return {
                "message": f"Dr. {dentist['name']} is not available on {day_name}",
                "available_slots": []
            }

    # All possible time slots
    all_slots = ["9:00 AM", "10:00 AM", "11:00 AM","12:00 PM", "2:00 PM", "3:00 PM","4:00 PM", "5:00 PM"
    ]

    # Get booked slots for this dentist on this date
    if appointments_df is not None and not appointments_df.empty:
        booked_slots = appointments_df[
            (appointments_df['dentistId'] == dentist_id) &
            (appointments_df['date'] == date) &
            (appointments_df['status'] != 'cancelled')
        ]['time'].tolist()
    else:
        booked_slots = []

    # Remove booked slots from all slots
    free_slots = [s for s in all_slots if s not in booked_slots]

    return {
        "dentist_id": dentist_id,
        "dentist_name": dentist['name'],
        "date": date,
        "day": day_name,
        "booked_slots": booked_slots,
        "available_slots": free_slots,
        "total_available": len(free_slots)
    }


# Get price estimate for a service
def get_price_estimate(service_name: str):

    if services_df is None:
        return {"message": "Database not connected"}

    # Find service
    service = services_df[services_df['name'] == service_name]

    if service.empty:
        return {
            "message": "Service not found",
            "available_services": services_df['name'].tolist()
        }

    service = service.iloc[0]

    return {
        "service": service['name'],
        "price": int(service['price']),
        "duration": service['duration'],
        "description": service.get('description', ''),
        "currency": "PKR"
    }


# Analyze patient visit history and predict next visit
def get_patient_pattern(user_id: str):

    if appointments_df is None:
        return {"message": "Database not connected"}

    # Get all visits for this user
    user_visits = appointments_df[
        appointments_df['userId'] == user_id
    ].copy()

    # New patient with no history
    if user_visits.empty:
        return {
            "userId": user_id,
            "message": "New patient - no history found",
            "total_visits": 0,
            "predicted_next_visit": (
                datetime.now() + timedelta(days=30)
            ).strftime("%Y-%m-%d"),
            "pattern": "First visit - next suggested after 1 month"
        }

    # Sort visits by date
    user_visits['date'] = pd.to_datetime(
        user_visits['date'], errors='coerce'
    )
    user_visits = user_visits.dropna(subset=['date'])
    user_visits = user_visits.sort_values('date')

    total_visits = len(user_visits)
    last_visit = user_visits['date'].iloc[-1]

    # Only one visit found
    if total_visits == 1:
        predicted_next = last_visit + timedelta(days=30)
        return {
            "userId": user_id,
            "total_visits": total_visits,
            "last_visit": last_visit.strftime("%Y-%m-%d"),
            "predicted_next_visit": predicted_next.strftime("%Y-%m-%d"),
            "pattern": "Only 1 visit - next suggested after 1 month"
        }

    # Calculate average gap between visits
    dates = user_visits['date'].tolist()
    gaps = []
    for i in range(1, len(dates)):
        gap = (dates[i] - dates[i - 1]).days
        gaps.append(gap)

    avg_gap = int(sum(gaps) / len(gaps))
    predicted_next = last_visit + timedelta(days=avg_gap)

    # Identify visit pattern
    if avg_gap <= 30:
        pattern = "Monthly visitor"
    elif avg_gap <= 60:
        pattern = "Every 2 months visitor"
    elif avg_gap <= 90:
        pattern = "Quarterly visitor"
    else:
        pattern = "Occasional visitor"

    # Get service names from visit history
    service_names = []
    if services_df is not None:
        for sid in user_visits['serviceId'].values:
            service = services_df[services_df['service_id'] == str(sid)]
            if not service.empty:
                service_names.append(service.iloc[0]['name'])

    return {
        "userId": user_id,
        "total_visits": total_visits,
        "last_visit": last_visit.strftime("%Y-%m-%d"),
        "average_gap_days": avg_gap,
        "predicted_next_visit": predicted_next.strftime("%Y-%m-%d"),
        "pattern": pattern,
        "services_taken": service_names
    }