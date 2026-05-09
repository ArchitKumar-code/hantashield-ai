from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from risk_engine import calculate_hantavirus_risk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "HantaShield AI Backend Running"
    }

@app.get("/analyze")
def analyze(city: str):

    result = calculate_hantavirus_risk(city)

    return result