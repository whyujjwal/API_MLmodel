from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
from app.model_utils import predict

router = APIRouter()

class PredictionInput(BaseModel):
    ID: int #as instructec on call 
    
@router.get("/region/{region_id}")
def read_item(region_id: int):
    return {"region_id": region_id}

@router.post("/predict")
def predict_endpoint(input: PredictionInput):
    try:
        # Convert input to DataFrame for model prediction
        input_data = pd.DataFrame([input.dict()])
        prediction = predict(input_data)
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
