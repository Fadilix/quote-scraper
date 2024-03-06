import scrapy
from quotescraper.items import QuoteItem

class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css("div.quote")
        
        for quote in quotes:

            # Creating a quote item
            quote_item = {
                "quote_text": quote.css("span.text::text").get(),
                "author": quote.css("span small.author::text").get(),
                "tags": quote.css(".tags a::text").getall(),
            }

            # url to access the author's page
            # And get some additional information
            url = quote.css("span a::attr(href)").get()
            yield response.follow(url, callback=self.parse_author_page, meta={"quote_item" : quote_item})

        next_page = response.css("li.next a::attr(href)").get()

        # Continue iterating through the pages until there are no more
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_author_page(self, response):
        # instance of quoteItem
        q_item = QuoteItem()

        quote_item = response.meta.get("quote_item", {})

        author_born_date =  response.css("span.author-born-date::text").get()
        author_born_location = response.css("span.author-born-location::text").get()
        author_description = response.css("div.author-description::text").get()

        q_item["quote_text"] = quote_item["quote_text"]
        q_item["author"] = quote_item["author"]
        q_item["tags"] = quote_item["tags"]
        q_item["author_born_date"] = author_born_date
        q_item["author_born_location"] = author_born_location
        q_item["author_description"] = author_description

        yield q_item