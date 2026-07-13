import os
import psutil
from fastapi import FastAPI
from pydantic import BaseModel

HEALTH_CHECK_ENDPOINT = os.getenv("HEALTH_CHECK_ENDPOINT", "/health")

app = FastAPI()


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    output: str


class MetricsResponse(BaseModel):
    cpu_usage: float
    memory_usage: float


@app.get(HEALTH_CHECK_ENDPOINT)
def health_check():
    return {"status": "ok"}


@app.get("/metrics")
def metrics() -> MetricsResponse:
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
    }


@app.post("/predict")
def predict(payload: PredictRequest) -> PredictResponse:
    output = payload.text.upper()
    return {"output": output}
