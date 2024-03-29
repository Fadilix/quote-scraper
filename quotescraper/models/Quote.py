from sqlalchemy import Column, String, Integer, ARRAY, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quote_text = Column(String(255))
    author = Column(String(255))
    tags = Column(ARRAY(String))
    author_born_date = Column(String(255))
    author_born_location = Column(String(255))
    author_description = Column(TEXT)