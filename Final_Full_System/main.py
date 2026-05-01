from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import (
    recommend_dentist,
    get_available_slots,
    get_price_estimate,
    get_patient_pattern,
    services_df
)

app = FastAPI(
    title="Miller Dental AI API",
    description="AI-powered dental recommendation system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    available_services = []
    if services_df is not None:
        available_services = services_df['name'].tolist()
    return {
        "message": "Miller Dental AI API is running",
        "available_services": available_services,
        "endpoints": [
            "/ai/recommend-dentist?service=Teeth Whitening",
            "/ai/available-slots?dentist_id=ID&date=2024-01-15",
            "/ai/price-estimate?service=Teeth Whitening",
            "/ai/patient-pattern?user_id=ID"
        ]
    }


@app.get("/ai/recommend-dentist")
def get_dentist_recommendation(
    service: str = Query(
        ...,
        description="Service name from database"
    ),
    top_n: int = Query(
        default=3,
        description="Number of recommendations to return"
    )
):
    if not service.strip():
        raise HTTPException(
            status_code=400,
            detail="Service name cannot be empty"
        )

    result = recommend_dentist(service, top_n)
    return result


@app.get("/ai/available-slots")
def available_slots(
    dentist_id: str = Query(
        ...,
        description="Dentist ID from database"
    ),
    date: str = Query(
        ...,
        description="Date in YYYY-MM-DD format"
    )
):
    if not dentist_id.strip() or not date.strip():
        raise HTTPException(
            status_code=400,
            detail="dentist_id and date are required"
        )

    result = get_available_slots(dentist_id, date)
    return result


@app.get("/ai/price-estimate")
def price_estimate(
    service: str = Query(
        ...,
        description="Service name from database"
    )
):
    if not service.strip():
        raise HTTPException(
            status_code=400,
            detail="Service name cannot be empty"
        )

    result = get_price_estimate(service)
    return result


@app.get("/ai/patient-pattern")
def patient_pattern(
    user_id: str = Query(
        ...,
        description="User ID from database"
    )
):
    if not user_id.strip():
        raise HTTPException(
            status_code=400,
            detail="User ID cannot be empty"
        )

    result = get_patient_pattern(user_id)
    return result