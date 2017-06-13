import scrapy
import csv


#
#  https://www.thoughtco.com/german-words-in-written-vocabulary-4071331
#
# source activate scanki
# scrapy crawl top100words
#
from scrapy.selector import HtmlXPathSelector


class top100words(scrapy.Spider):
    name = "top100words"
    start_urls = [
        'https://www.thoughtco.com/german-words-in-written-vocabulary-4071331',
    ]

    def parse(self, response):


        hxs = HtmlXPathSelector(response)
        tables = hxs.select('//tbody')

        tables.pop(0)
        rows = tables[0].select('./tr')


        with open(self.name + '.csv', 'a') as csvfile:
            fieldnames = ['German','English']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            i = 0
            for row in rows:
                items = row.select('./td/text()').extract()
                print(items)
                writer.writerow({'German': items[0],'English':items[1]})



