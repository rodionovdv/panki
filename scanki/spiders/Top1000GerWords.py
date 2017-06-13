import scrapy
import csv

#
#  http://www.languagedaily.com/learn-german/vocabulary/common-german-words
#
# source activate scanki
# scrapy crawl Top1000GermWords
#

class Top1000GerWords(scrapy.Spider):
    name = "Top1000GermWords"
    start_urls = [
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words',
            'http://www.languagedaily.com/learn-german/vocabulary/most-common-german-words-2',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-3',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-4',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-5',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-6',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-7',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-8',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-9',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-10',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-11',
            'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-12',
        ]


    def parse(self, response):
        page = response.url.split("/")[-2]

        words = response.xpath('//td[@class="bigLetter"]/text()').extract()

        with open('Top1000GermWords.csv', 'a') as csvfile:
            fieldnames = ['German']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            i = 0
            for word in words:


                writer.writerow({'German':word})



        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)