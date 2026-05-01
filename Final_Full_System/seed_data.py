from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

db = client["test"]   


def seed_data():

    services = [
        {
            "serviceName": "Teeth Whitening",
            "price": 15000,
            "duration": "45 minutes",
            "description": "Professional teeth whitening treatment"
        },
        {
            "serviceName": "Dental Implants",
            "price": 80000,
            "duration": "2 hours",
            "description": "Permanent tooth replacement solution"
        },
        {
            "serviceName": "Crown & Bridges",
            "price": 25000,
            "duration": "1 hour",
            "description": "Dental crown and bridge placement"
        },
        {
            "serviceName": "Cleaning & Check Up",
            "price": 5000,
            "duration": "30 minutes",
            "description": "Routine dental cleaning and examination"
        },
        {
            "serviceName": "Clear Braces",
            "price": 120000,
            "duration": "Ongoing",
            "description": "Invisible orthodontic braces treatment"
        },
        {
            "serviceName": "Oral Surgical",
            "price": 50000,
            "duration": "1.5 hours",
            "description": "Oral surgery and tooth extraction"
        },
        {
            "serviceName": "Cosmetic Dentistry",
            "price": 30000,
            "duration": "1.5 hours",
            "description": "Complete smile makeover treatment"
        }
    ]

    service_result = db.services.insert_many(services)
    service_ids = service_result.inserted_ids


    dentists = [
        {
            "name": "Dr. Sarah Johnson",
            "specialty": "Cosmetic Dentistry",
            "experience": "8 years",
            "availableDays": ["Monday", "Tuesday", "Wednesday"],
            "availableTime": "10:00 AM - 6:00 PM",
            "image": "doctor1.jpg"
        },
        {
            "name": "Dr. Bradley Miller",
            "specialty": "General Dentistry",
            "experience": "15 years",
            "availableDays": ["Monday", "Wednesday", "Friday"],
            "availableTime": "9:00 AM - 5:00 PM",
            "image": "doctor2.jpg"
        },
        {
            "name": "Dr. Emily Chen",
            "specialty": "Orthodontist",
            "experience": "6 years",
            "availableDays": ["Tuesday", "Thursday", "Saturday"],
            "availableTime": "11:00 AM - 7:00 PM",
            "image": "doctor3.jpg"
        },
        {
            "name": "Dr. Michael Brown",
            "specialty": "Oral Surgeon",
            "experience": "10 years",
            "availableDays": ["Monday", "Tuesday", "Friday"],
            "availableTime": "8:00 AM - 4:00 PM",
            "image": "doctor4.jpg"
        },
        {
            "name": "Dr. Lisa Parker",
            "specialty": "Periodontist",
            "experience": "7 years",
            "availableDays": ["Wednesday", "Thursday", "Saturday"],
            "availableTime": "10:00 AM - 6:00 PM",
            "image": "doctor5.jpg"
        }
    ]

    dentist_result = db.dentists.insert_many(dentists)
    dentist_ids = dentist_result.inserted_ids


    users = [
        {
            "name": "Ali Khan",
            "email": "ali@email.com",
            "password": "hashed_password_123",
            "role": "user",
            "phoneNumber": "03001234567"
        },
        {
            "name": "Sara Ahmed",
            "email": "sara@email.com",
            "password": "hashed_password_456",
            "role": "user",
            "phoneNumber": "03009876543"
        },
        {
            "name": "Ahmed Raza",
            "email": "ahmed@email.com",
            "password": "hashed_password_789",
            "role": "user",
            "phoneNumber": "03331234567"
        }
    ]

    user_result = db.users.insert_many(users)
    user_ids = user_result.inserted_ids


    appointments = [
        {
            "userId": user_ids[0],
            "dentistId": dentist_ids[0],
            "serviceId": service_ids[0],
            "date": "2024-01-15",
            "time": "10:00 AM",
            "status": "confirmed"
        },
        {
            "userId": user_ids[0],
            "dentistId": dentist_ids[0],
            "serviceId": service_ids[1],
            "date": "2024-01-15",
            "time": "11:00 AM",
            "status": "confirmed"
        },
        {
            "userId": user_ids[1],
            "dentistId": dentist_ids[1],
            "serviceId": service_ids[2],
            "date": "2024-01-20",
            "time": "9:00 AM",
            "status": "confirmed"
        },
        {
            "userId": user_ids[0],
            "dentistId": dentist_ids[0],
            "serviceId": service_ids[3],
            "date": "2023-12-10",
            "time": "2:00 PM",
            "status": "completed"
        }
    ]

    db.appointments.insert_many(appointments)

    print("All data inserted successfully!")


if __name__ == "__main__":
    seed_data()