from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import get_price_estimate, recommend_dentist , get_available_slots , get_patient_pattern


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
    return {
        "message": "Miller Dental AI API Running!"
    }

@app.get("/ai/recommend-dentist")
def get_dentist_recommendation(
    service: str = Query(
        ...,
        description="Service name e.g. Teeth Whitening"
    ),
    top_n: int = Query(
        default=3,
        description="Number of recommendations"
    )
):
    if not service:
        raise HTTPException(
            status_code=400,
            detail="Service name required!"
        )

    result = recommend_dentist(service, top_n)
    return result

@app.get("/ai/available-slots")
def available_slots(
    dentist_id: int = Query(
        ...,
        description="Dentist ID"
    ),
    date: str = Query(
        ...,
        description="Date in YYYY-MM-DD format"
    )
):
    if not dentist_id or not date:
        raise HTTPException(
            status_code=400,
            detail="dentist_id and date required!"
        )

    result = get_available_slots(dentist_id, date)
    return result


@app.get("/ai/price-estimate")
def price_estimate(
    service: str = Query(
        ...,
        description="Service name"
    )
):
    result = get_price_estimate(service)
    return result


@app.get("/ai/patient-pattern")
def patient_pattern(
    user_id: int = Query(
        ...,
        description="User ID"
    )
):
    result = get_patient_pattern(user_id)
    return result