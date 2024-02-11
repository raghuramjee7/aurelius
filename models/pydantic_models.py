from pydantic import BaseModel, Field 

class KeyOut(BaseModel):
    key: int
    message: str = Field(default='Please use this key to get a random quote.')
    
class QuoteIn(BaseModel):
    key: int

class QuoteOut(BaseModel):
    key: int
    quote: str