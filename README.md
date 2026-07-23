# Backend Invernadero

## Instalación
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Correr el servidor
\`\`\`bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
\`\`\`

## Endpoints
- POST /api/lecturas — recibe lecturas de sensores del ESP32