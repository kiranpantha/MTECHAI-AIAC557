# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SabjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # ["गोलभेडा ठूलो(नेपाली)", "के.जी.", "रू ६०.००", "रू ७०.००", "रू ६५.००"]
    date = scrapy.Field()
    name = scrapy.Field()
    weightUnit = scrapy.Field()
    minimumAmount = scrapy.Field()
    maximumAmount = scrapy.Field()
    averageAmount = scrapy.Field()
    pass
