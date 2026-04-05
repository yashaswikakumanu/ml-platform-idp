from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ML API is running"}

@app.get("/predict")
def predict():
    return {"prediction": 42}
    