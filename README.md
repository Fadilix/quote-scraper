# Quote Scraper with `Scrapy`

# Scrapy ?

Scrapy is an open-source web crawling and scraping framework for Python, designed to facilitate the extraction of data from websites. 

## Overview
The Quote Scraper project utilizes Scrapy to gather quotes and related information from quotes.toscrape.com. The spider navigates through the website, extracting details such as quote text, author, tags, birth date, birth location, and author description. The data is then stored in both a PostgreSQL database and a JSON file, providing users with flexibility in data storage options. This project serves as a practical example of web scraping using Scrapy, demonstrating its capability to efficiently navigate and collect structured data from a website, and showcases best practices for storing the scraped information in a relational database and a backup JSON file.

## Requirements
* Python 3.x
* Scrapy
* SQLAlchemy

## Database setup
- Create a `database` with a name you want
  
- open `quotescraper\settings.py` file.
  
- Locate the `DATABASE_URL` variable.
  
- Replace the existing database URL with your own PostgreSQL database connection details.
  ```python
  DATABASE_URL = "{dialect}://{username}:{password}@{host}:{post}/{db_name}"
  ```   

## `Quote` table structure :
```python
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
```

## Usage
- Install the required dependencies
  ```bash
  pip install -r requirements.txt
  ```
- Go into the spiders folders
  ```bash
  cd .\quotescraper\spiders\
  ```
- Run the spider to scrape quotes and store them in the database:
  ```bash
  scrapy crawl quote
  ```

## `PostgreSQL` pipeline to store the data in the database :
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from quotescraper.settings import DATABASE_URL

from quotescraper.models.Quote import Quote
class PostgreSQLPipeline:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        session = self.Session()
        quote = Quote(**item)

        try:
            session.add(quote)
            session.commit()
        except Exception as e:
            session.rollback()
            spider.log(f"Error while adding the data: {e}")
        finally:
            session.close()
        
        return item
```

## Sample of `json` response (`data.json` file) :
```json
  {
    "quote_text": "“What really knocks me out is a book that, when you're all done...”",
    "author": "J.D. Salinger",
    "tags": ["authors", "books", "literature", "reading", "writing"],
    "author_born_date": "January 01, 1919",
    "author_born_location": "in Manhattan, New York, The United States",
    "author_description": "Jerome David Salinger was an American author, best known for his 1951 nov..."
  },
```



  
