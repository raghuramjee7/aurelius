from pydantic import BaseModel 

class QuoteIn(BaseModel):
    key: str

class QuoteOut(BaseModel):
    key: str
    quote: str