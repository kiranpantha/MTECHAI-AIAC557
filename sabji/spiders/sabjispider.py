import scrapy
import pandas as pd
from datetime import datetime
from sabji.items import SabjiItem
import sqlite3



class SabjispiderSpider(scrapy.Spider):
    name = "sabjispider"
    allowed_domains = ["kalimatimarket.gov.np"]

    date_list = pd.date_range(end = datetime.today(), periods = 10).to_pydatetime().tolist()
    date_index = 0
    token = ''

    start_urls = ['https://kalimatimarket.gov.np/price']

    def parse(self, response):
        self.token = response.css('#csrf::attr(value)').get()
        # print({'datePricing': self.date_list[self.date_index].strftime("%Y-%m-%d"),'_token':token})
        for date_list_ in self.date_list:
            yield scrapy.FormRequest.from_response(
                response,
                formdata={'datePricing': date_list_.strftime("%Y-%m-%d"),'_token':self.token},
                meta={'datePricing': date_list_.strftime("%Y-%m-%d")},
                callback=self.post_parse,
            )

    def post_parse(self,response):
        datePricing = response.meta.get('datePricing')
        kalimati_wrapper = response.css('#commodityPriceParticular')
        data_sabji = []
        for kalimati_tbody in kalimati_wrapper.css('tbody'):
            for kalimati_tr in kalimati_tbody.css('tr'):
                sabji_item = SabjiItem()
                sabji_item['date'] = datePricing
                sabji_item['name'] = (kalimati_tr.css('td::text')[0]).get()
                sabji_item['weightUnit'] = (kalimati_tr.css('td::text')[1]).get()
                sabji_item['minimumAmount'] = (kalimati_tr.css('td::text')[2]).get()
                sabji_item['maximumAmount'] = (kalimati_tr.css('td::text')[3]).get()
                sabji_item['averageAmount'] = (kalimati_tr.css('td::text')[4]).get()
                
                # print(kalimati_tr.css('td::text')[2])
                # for kalimati_td in kalimati_tr.css('td::text'):
                    # print(kalimati_td.get())
                    # data_sabji_temp.append(kalimati_td.get())
                data_sabji.append(sabji_item)
                self.save_to_database(sabji_item)

        yield {'datePricing':data_sabji}


    def save_to_database(self, item):
        conn = sqlite3.connect('my_data.sqlite3')
        c = conn.cursor()

        # Insert the scraped data into the 'scraped_data' table
        c.execute('''
            INSERT INTO scraped_data (date, name, weightUnit, minimumAmount, maximumAmount, averageAmount)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            item['date'],
            item['name'],
            item['weightUnit'],
            item['minimumAmount'],
            item['maximumAmount'],
            item['averageAmount'],
        ))

        conn.commit()
        conn.close()