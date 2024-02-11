from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import model, connect
import logging
import sys
from .quotes import quotes_app
import src.util as util


app = FastAPI()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

model.Base.metadata.create_all(bind = connect.engine) 
logger.info("Database connection is set")

logger.info("Preprocessing the data")
util.preprocessing()
logger.info("Preprocessing is done")

user_data = {}

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
        "message": "Welcome to Quotes API, Please take a look at the documentation to get started."
    }

app.include_router(quotes_app.router)