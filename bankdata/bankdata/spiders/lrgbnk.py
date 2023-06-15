import scrapy
import csv


class LrgbnkSpider(scrapy.Spider):
    name = 'lrgbnk'
    allowed_domains = ['federalreserve.gov']
    start_urls = [
        'https://www.federalreserve.gov/releases/lbr/current/default.htm']

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table = child
                break

        count = 0

        csv_file = open('banks.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(['bank', 'rank', 'hq city', 'tot assets',
                        'dom assets', 'dom branches', 'tot branches'])

        for row in table.xpath('//tr'):
            if count > 200:
                break
            try:
                bank = row.xpath('td//text()')[0].extract()
                rank = row.xpath('td//text()')[1].extract()
                hq = row.xpath('td//text()')[3].extract()
                tot_assets = row.xpath('td//text()')[5].extract()
                dom_assets = row.xpath('td//text()')[6].extract()
                dom_branches = row.xpath('td//text()')[9].extract()
                tot_branches = row.xpath('td//text()')[10].extract()
                writer.writerow([bank, rank, hq, tot_assets,
                                dom_assets, dom_branches, tot_branches])
                print(count)
                count += 1
            except IndexError:
                pass
        csv_file.close()
