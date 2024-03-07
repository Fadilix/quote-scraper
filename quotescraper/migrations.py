from models.Quote import Base
from sqlalchemy import create_engine
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(e)