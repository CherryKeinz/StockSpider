#-*- coding: utf-8 -*-
import scrapy
# import 要改为items.py中定义的类名
from stockSpider.items import stockItem
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spriderDemo(scrapy.spiders.Spider):
    # -name: 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    # 命令行中 scrapy crawl + name
    name = "spider"
    allowed_domains = ["http://quote.stockstar.com"]
    start_urls = []
    start_urls.append('http://quote.stockstar.com/stock/ranklist_a_3_1_1.html')
    # 这里是分页的每个url
    # for i in  range(1,5):
    #     start_urls.append('http://10.3.210.84:4237/UserCenter/usercenter?querytype=1&querypolicyid=20131113132814&type=get&query=0025&query=&gx=OR&st=4efb610f4e0081f4&st=4efb610f4e0081f4&region=20131113132006&region=20131113132006&treeid=20131021155159&updatetime=0&datapid=&imtime=0&dataj=&tpf=Y&nodeid=20040921165456&username=guest&password=null&viewjbid=55555555555555&order=&orderdsc=&iswhole=0&resnum=20&maxnum=50000&pagenum='+
    #                       str(i) + '&presnum='+ str(20*i) +'&qy0=0025&qy1=')
    custom_settings = {
		'ITEM_PIPELINES' : {
            # settings.py中BOT_NAME的名字..pipelines.JsonWithEncodingPipeline
			'stockSpider.pipelines.JsonWithEncodingPipeline':100,	# 开通CrawlerStorePipeline
			},
        'DOWNLOADER_MIDDLEWARES' :{
        'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'stockSpider.middlewares.MyUserAgentMiddleware': 400,
        }
	}
    def parse(self, response):
        items = []
 #//*[@id="fixed"]
        for site in response.xpath('//div[@class="bg_box"]/div/table/tbody/tr'):
            item = stockItem()

            # count += 1
            # if count == 21:
            #     break
            # item['name'] = site.xpath('LCONTENT/text()').extract()[0]
            # //*[@id="datalist"]/tr[1]/td[1]/a
            id = site.xpath('td/a/text()')

            item['symbol'] = id.extract()[0]
            item['name'] = site.xpath('td[2]/a/text()').extract()[0]
            item['price'] = site.xpath('td[3]/span/text()').extract()[0]
            item['change'] =  site.xpath('td[4]/span/text()').extract()[0]
            item['chg'] =  site.xpath('td[5]/span/text()').extract()[0]
            # item['amplitude'] =
            item['volume'] =   site.xpath('td[7]/text()').extract()[0]
            item['turnover'] =  site.xpath('td[8]/text()').extract()[0]
            # item['preclose'] =
            # item['open'] =
            # item['higheset'] =
            # item['loweset'] =
            item['changeinfive'] = site.xpath('td[6]/span/text()').extract()[0]

            items.append(item)

        return items

    #
    # def parse_more(self,response):
    #     item = response.meta['item']
    #     name = response.xpath('//CONTENT[1]/text()')
    #     author = response.xpath('//LCONTENT/text()')
    #     item['name'] = name.extract()[0]
    #     # 判断HTML标签内容为空，跳过空的
    #     if author.extract():
    #         item['author'] =  author.extract()[0]
    #     # item["url_id"] = response.xpath('//div[@class="main"]/div[@class="info"]/table[@class="table-1"]/tr[2]/td/text()').extract()[0]
    #     # site = response.xpath('//div[@class="detail"]/div[@class="info"]/table[@class="table-1"]')
    #     # item["url_name"] = site.xpath('tr[1]/td/text()').extract()[0]
    #     # item['url_enterprise'] = site.xpath('tr[2]/td/a[1]/text()').extract()[0]
    #     # item['url_function'] = site.xpath('tr[3]/td/text()').extract()[0]
    #     # item['url_usage'] = site.xpath('tr[4]/td/text()').extract()[0]
    #
    #     yield item