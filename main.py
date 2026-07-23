from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Lectura(BaseModel):
    device_id: str
    humedad_suelo: float
    temperatura_ambiente: float
    humedad_ambiente: float

@app.post("/api/lecturas")
async def recieve_lecture(lectura: Lectura):
    print(f"Recibido de {lectura.device_id}: {lectura}")
    return {"status": "recibido"}
