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
import os
class PostgreSQLPipeline():
    def __init__(self) -> None:
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.Session = sessionmaker(bind=self.engine)
    

    def process_item(self, item, spider):
        session = self.Session()
        