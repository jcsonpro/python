# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HanbitMediaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_translator = scrapy.Field()
    book_pub_date = scrapy.Field()
    book_isbn = scrapy.Field()
    pass
