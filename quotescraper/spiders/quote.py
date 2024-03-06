import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css("div.quote")

        for quote in quotes:
            yield {
                "text" : quote.css("span.text::text").get(),
                "author": quote.css("span small.author::text").get(),
                "tags": quote.css(".tags a::text").getall()
            }
