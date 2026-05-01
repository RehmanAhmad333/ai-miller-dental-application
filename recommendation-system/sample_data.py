# sample_data.py

dentists = [
    {
        "dentist_id": 1,
        "name": "Dr. Sarah Johnson",
        "specialty": "Cosmetic Dentistry",
        "experience": 8,
        "availableDays": ["Monday", "Tuesday", "Wednesday"],
        "availableTime": "10:00 AM - 6:00 PM",
        "services": ["Teeth Whitening", "Clear Braces", "Cosmetic Dentistry"]
    },
    {
        "dentist_id": 2,
        "name": "Dr. Bradley Miller",
        "specialty": "General Dentistry",
        "experience": 15,
        "availableDays": ["Monday", "Wednesday", "Friday"],
        "availableTime": "9:00 AM - 5:00 PM",
        "services": ["Cleaning & Check Up", "Dental Implants", "Crown & Bridges"]
    },
    {
        "dentist_id": 3,
        "name": "Dr. Emily Chen",
        "specialty": "Orthodontist",
        "experience": 6,
        "availableDays": ["Tuesday", "Thursday", "Saturday"],
        "availableTime": "11:00 AM - 7:00 PM",
        "services": ["Clear Braces", "Crown & Bridges"]
    },
    {
        "dentist_id": 4,
        "name": "Dr. Michael Brown",
        "specialty": "Oral Surgeon",
        "experience": 10,
        "availableDays": ["Monday", "Tuesday", "Friday"],
        "availableTime": "8:00 AM - 4:00 PM",
        "services": ["Oral Surgical", "Dental Implants"]
    },
    {
        "dentist_id": 5,
        "name": "Dr. Lisa Parker",
        "specialty": "Periodontist",
        "experience": 7,
        "availableDays": ["Wednesday", "Thursday", "Saturday"],
        "availableTime": "10:00 AM - 6:00 PM",
        "services": ["Cleaning & Check Up", "Oral Surgical"]
    }
]

services = [
    {"service_id": 1, "name": "Teeth Whitening", "price": 15000, "duration": "45 minutes"},
    {"service_id": 2, "name": "Dental Implants", "price": 80000, "duration": "2 hours"},
    {"service_id": 3, "name": "Crown & Bridges", "price": 25000, "duration": "1 hour"},
    {"service_id": 4, "name": "Cosmetic Dentistry", "price": 30000, "duration": "1.5 hours"},
    {"service_id": 5, "name": "Cleaning & Check Up", "price": 5000, "duration": "30 minutes"},
    {"service_id": 6, "name": "Clear Braces", "price": 120000, "duration": "Ongoing"},
    {"service_id": 7, "name": "Oral Surgical", "price": 50000, "duration": "1.5 hours"}
]