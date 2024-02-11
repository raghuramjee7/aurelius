import sys
import logging
import PyPDF2
import json
from models.connect import get_db
from fastapi import Depends
from models.model import Quotes
from sqlalchemy.orm import Session

FILE_URL = "C:/Users/SAKET/Downloads/meditations.pdf"
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def generate_quote(pdf):

    logging.info("The number of pages are " + str(len(pdf.pages)))
    
    quotes = []

    for page in pdf.pages:
        text = page.extract_text()
        quotes_extracted = text.split(" \n \n")
        logging.info(str(len(text)) + " characters extracted from the page")
        logging.info("Quotes are " + str(len(quotes)))
        for quote in quotes_extracted:
            quote = quote.replace("\n", "")
            quotes.append(quote)
    
    with open("quotes.json", "w") as file:
        json.dump(quotes, file)
        logging.info("Data written to quotes.json file")
        logging.info("The number of quotes are " + str(len(quotes)))

    return None

def dump_data(db):
    quotes = json.load(open("quotes.json"))
    
    for quote in quotes:
        quote = Quotes(quote = quote)
        db.add(quote)
        db.commit()
        db.refresh(quote)
    return None

def start(db):
    pdf_obj = open(FILE_URL, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_obj)
    logging.info("File object created successfully")

    generate_quote(pdf_reader)
    logging.info("Quotes generated successfully and saved in quotes.json file")

    logging.info("Initialising data dump into db")
    dump_data(db)
    logging.info("Data dump into db successful")
    return None








