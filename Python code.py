from fastapi import FastAPI
from typing import List
import random

app = FastAPI()


def get_sensor_data():
    return [random.choice([True, False]) for _ in range(10)]  

@app.get("/")
def read_root():
    return {"message": "Smart Parking System"
            " - by Pavithran"}
    

@app.get("/status", response_model=List[dict])
def read_status():
    sensor_data = get_sensor_data()
    parking_status = [{'spot': i + 1, 'occupied': occupied} for i, occupied in enumerate(sensor_data)]
    return parking_status

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
