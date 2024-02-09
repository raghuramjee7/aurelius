from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import model, connect

app = FastAPI()

model.Base.metadata.create_all(bind = connect.engine) 

# CORS
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # allow all http methods
    allow_headers=["*"], # allow all http headers
)

@app.get("/")
async def home():
    return {
        "message": "Welcome to Quotes API"
    }