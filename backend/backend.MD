# How to start the backend
* cd backend
* python -m venv venv
* venv\Scripts\activate
* pip install fastapi uvicorn
* pip install pydantic python-dotenv sqlalchemy

## simple load
uvicorn app.main:app --reload


## Production run (no reload)
uvicorn app.main:app --host 0.0.0.0 --port 8000

## Next tasks
* Connect FastAPI to PostgreSQL

* JWT authentication

* Dockerize FastAPI

* Async background tasks

* Serve ML models / YOLO / LLMs via FastAPI

* FastAPI + Nginx + HTTPS
