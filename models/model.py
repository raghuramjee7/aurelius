from .connect import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text

class Quotes(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    quote = Column(String, nullable=False)