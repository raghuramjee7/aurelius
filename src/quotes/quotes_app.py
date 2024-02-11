from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from models.model import Quotes
from models.connect import get_db
from models.pydantic_models import QuoteIn, QuoteOut, KeyOut
from src.util import generate_uid
import random, logging, sys

router = APIRouter(
    prefix="/quotes",
    tags = ["Quotes"]
)

user_data = {}

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@router.get("/", response_model = QuoteOut)
async def get_quote(req: QuoteIn, db: Session = Depends(get_db)):
    
    user_key = req.key
    logger.info(f"User key: {user_key}")

    size = db.query(Quotes).count()
    if user_key not in user_data:
        user_data[user_key] = set()

    while True:
        random_index = random.randint(0, size-1)
        if random_index in user_data[user_key]:
            continue
        quote = db.query(Quotes).filter(Quotes.id == random_index).first()
        if quote:
            break

    logger.info(f"Quote: {quote.quote}")
    user_data[user_key].add(random_index)

    result = QuoteOut(key = user_key, quote = quote.quote)
    return result

@router.get("/generate_key", response_model = KeyOut)
async def get_key():
    
    id = generate_uid()
    key = KeyOut(key=id)
    return key
