# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotescraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Trim the extra space of the author description
        author_description = adapter.get("author_description")
        new_author_description = author_description.strip()
        adapter["author_description"] = new_author_description
        
        return item


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