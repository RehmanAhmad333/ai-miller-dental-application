from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import recommend_dentist


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