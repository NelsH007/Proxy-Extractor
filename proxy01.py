# -*- coding: utf-8 -*-
import scrapy


class Proxy01Spider(scrapy.Spider):
    name = 'proxy01'
    start_urls = ['https://free-proxy-list.net/']

#((//*[@id="proxylisttable"]/tbody/tr)[3]/td)[5]

    def parse(self, response):
        rows = response.xpath('//*[@id="proxylisttable"]/tbody/tr')
        for row in rows[:180]:
            typeprox = row.xpath('./td/text()')[4].get()
            httpsl = row.xpath('./td/text()')[6].get()

            if typeprox == 'elite proxy' and htpsl == 'yes':
                ip = row.xpath('./td/text()')[0].get()
                port = row.xpath('./td/text()')[1].get()
                proxy = ip+':'+port
                yield {'proxy': proxy,
                       'type': typeprox}
