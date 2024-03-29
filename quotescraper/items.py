# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuoteItem(scrapy.Item):
    quote_text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    author_born_date = scrapy.Field()
    author_born_location = scrapy.Field()
    author_description = scrapy.Field()

