import scrapy


class SabjispiderSpider(scrapy.Spider):
    name = "sabjispider"
    allowed_domains = ["kalimatimarket.gov.np"]

    start_urls = ['https://kalimatimarket.gov.np/price#']

    data_sabji = []

    def parse(self, response):
        kalimati_wrapper = response.css('#commodityPriceParticular');
        for kalimati_tbody in kalimati_wrapper.css('tbody'):
            for kalimati_tr in kalimati_tbody.css('tr'):
                data_sabji_temp = []
                for kalimati_td in kalimati_tr.css('td::text'):
                    data_sabji_temp.append(kalimati_td.get())
                self.data_sabji.append(data_sabji_temp)
        yield {'data':self.data_sabji}
