# -*- coding: utf-8 -*-
from translate.TranslatorInterface import TranslatorInterface
import requests
from lxml import html
import json
from gtts import gTTS


#
# https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20170611T172307Z.4abaf98a6a837032.37092569e629450212c2a109f3e90091d784d1e3&lang=ru-de&text=ножницы
#
#
class Translator(TranslatorInterface):
    def translate(self, word, _from, _to, folder):

        # Yandex translate + TTS mp3
        payload = {'key': 'dict.1.1.20170611T172307Z.4abaf98a6a837032.37092569e629450212c2a109f3e90091d784d1e3',
                   'lang': _from + '-' + _to, 'text': word}
        r = requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/lookup', params=payload)
        # print(r.url)

        resp = r.json()

        audio = word

        if 'gen' in resp['def'][0]:
            if resp['def'][0]['gen'] == 'f':
                audio = 'die ' + word
            if resp['def'][0]['gen'] == 'm':
                audio = 'der ' + word
            if resp['def'][0]['gen'] == 'n':
                audio = 'das ' + word
        tts = gTTS(text=audio, lang=_from, slow=False)
        tts.save('./' + folder + '/' + word + '.mp3')

        trans = resp['def'][0]['tr'][0]['text']

        # Glosbe examples
        payloadgl = {'from': _from, 'dest': _to, 'format': 'json', 'phrase': word, 'pretty': 'true', 'tm': 'true'}
        rg = requests.get('https://glosbe.com/gapi/translate', params=payloadgl)
        # print(rg.url)

        example = ''
        if 'ex' in resp['def'][0]['tr'][0]:
            example = resp['def'][0]['tr'][0]['ex'][0]['text']

        # Example http://dict.tu-chemnitz.de/dings.cgi?o=302;service=deen;iservice=de-en-ex;query=k%C3%B6nnen

        # rex = requests.get('http://dict.tu-chemnitz.de/dings.cgi?o=302;service=deen;iservice=de-en-ex;query='+word)
        # tree = html.fromstring(rex.text)
        # html_element = tree.xpath(".//table[@id='result']")
        # html_element

        return {'German': audio.encode("utf-8"), 'Russian': trans.encode("utf-8"), 'GermanEx': example.encode("utf-8"),
                'GerAudio': ('[sound:' + word + '.mp3]').encode("utf-8")}
