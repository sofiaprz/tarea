from fastapi import FastAPI
app = FastAPI()

@app.get("/chateo")
def read_root():
    return {"Bien y tu?"}
