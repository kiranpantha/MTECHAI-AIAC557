import scrapy
import pandas as pd
from datetime import datetime



class SabjispiderSpider(scrapy.Spider):
    name = "sabjispider"
    allowed_domains = ["kalimatimarket.gov.np"]

    date_list = pd.date_range(end = datetime.today(), periods = 100).to_pydatetime().tolist()
    date_index = 0

    start_urls = ['https://kalimatimarket.gov.np/price#']

    data_sabji = []

    def parse(self, response):
        token = response.css('#csrf::attr(value)').get()
        print({'datePricing': self.date_list[self.date_index].strftime("%Y-%m-%d"),'_token':token})
        return scrapy.FormRequest.from_response(
            response,
            formdata={'datePricing': self.date_list[0].strftime("%Y-%m-%d"),'_token':token},
            callback=self.post_parse,
        )

    def post_parse(self,response):
        kalimati_wrapper = response.css('#commodityPriceParticular');
        for kalimati_tbody in kalimati_wrapper.css('tbody'):
            for kalimati_tr in kalimati_tbody.css('tr'):
                data_sabji_temp = []
                for kalimati_td in kalimati_tr.css('td::text'):
                    data_sabji_temp.append(kalimati_td.get())
                self.data_sabji.append(data_sabji_temp)
        yield {'data':self.data_sabji}
