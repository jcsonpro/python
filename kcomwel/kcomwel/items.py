# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KcomwelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 번호
    # st_no = scrapy.Field()
    # 제목
    st_title = scrapy.Field()
    # 저자
    st_author = scrapy.Field()
    # 목록
    st_index = scrapy.Field()
    # 요약
    st_summary = scrapy.Field()

    pass
