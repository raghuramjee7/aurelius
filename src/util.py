import logging
import random
import json
from models.connect import SessionLocal
from models.model import Quotes
from .generator.quote_generator import start

def generate_uid():
    return random.randint(100000, 999999)

def preprocessing():
    logging.info("Starting all checks")
    # Check if the database is empty
    db = SessionLocal()
    if db.query(Quotes).count() == 0:
        logging.info("Database is empty, starting the quote generator")
        start()
    else:
        logging.info("Database is not empty, no need to start the quote generator")

    # Loading all user data in memory
    #logging.info("Loading all user data in memory")
    #used_quotes = json.load(open("used_quotes.json", "r"))
    #return used_quotes
        
    return {}
