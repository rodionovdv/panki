import scrapy
import csv


#
#  http://www.thegermanprofessor.com/top-500-german-words/top-500-german-words-201-300/
#
# source activate scanki
# scrapy crawl thegermanprofessor
#

class thegermanprofessor(scrapy.Spider):
    name = "thegermanprofessor"
    start_urls = [
        'http://www.thegermanprofessor.com/top-500-german-words/',
        'http://www.thegermanprofessor.com/top-500-german-words/top-500-german-words-101-200/',
        'http://www.thegermanprofessor.com/top-500-german-words/top-500-german-words-201-300/',
        'http://www.thegermanprofessor.com/top-500-german-words/top-500-german-words-301-400/',
        'http://www.thegermanprofessor.com/top-500-german-words/top-500-german-words-401-500/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]

        words = response.xpath('//p/strong/text()').extract()
        words.pop(0)

        with open(self.name + '.csv', 'a') as csvfile:
            fieldnames = ['German']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            i = 0
            for word in words:
                writer.writerow({'German': word})



                # filename = 'quotes-%s.html' % page
                # with open(filename, 'wb') as f:
                #     f.write(response.body)
                # self.log('Saved file %s' % filename)
