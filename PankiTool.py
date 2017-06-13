from translate.Translator import Translator
import csv
import logging
import sys

if __name__ == "__main__":
    name = 'thegermanprofessor'
    logging.basicConfig(filename=name + '.log', level=logging.ERROR)

    reload(sys)
    sys.setdefaultencoding('utf-8')
    translator = Translator()

    with open('./' + name + '.txt') as f, open(name + '.csv', 'a') as csvfile:
        words = f.read().splitlines()
        size = len(words)

        fieldnames = ['German', 'Russian', 'GermanEx', 'GerAudio']
        writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=fieldnames)

        writer.writeheader()

        i = 0
        for word in words:
            try:
                result = translator.translate(word, 'de', 'ru',name)
                # print(result)

                writer.writerow(result)

                i += 1
                if i % 10 == 0:
                    print('Done ' + str(i) + '/' + str(size))
            except:
                logging.error(word)

        print('Done ' + str(i) + '/' + str(size))
