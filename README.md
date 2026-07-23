# Backend Invernadero

## Instalación
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Correr el servidor
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


## Endpoints
- POST /api/lecturas — recibe lecturas de sensores del ESP32