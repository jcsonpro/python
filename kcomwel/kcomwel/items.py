# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KcomwelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    st_title = scrapy.Field()
    st_content = scrapy.Field()

    pass
