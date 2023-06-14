import scrapy


class LrgbnkSpider(scrapy.Spider):
    name = 'lrgbnk'
    allowed_domains = ['federalreserve.gov']
    start_urls = [
        'https://www.federalreserve.gov/releases/lbr/current/default.htm']

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 200:
                table = child
                break
        count = 0
        for row in table.xpath('//tr'):
            try:
                print(row.xpath('td//text()').extract())
                print(count)
                count += 1
                if count > 20:
                    break
            except IndexError:
                pass
