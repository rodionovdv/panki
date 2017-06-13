import Queue
import os

import tornado.ioloop
import tornado.web
from handlers.MainHandler import MainHandler
from handlers.ui.UIHandler import UIHandler
from translate.Translator import YandexTranslator
from translate.GlosbeTranslator import GlosbeTranslator


def panki_app(translator, _from, _to):
    settings = {
        'debug': True,
        "static_path": os.path.join(os.path.dirname(__file__), "static"),

    }
    return tornado.web.Application(
        [
            (r'/', MainHandler),
            (r'/ui', UIHandler, {'translator': translator, '_from': _from, '_to':_to }),
            (r"/static/panki\.jpg", tornado.web.StaticFileHandler,
             {'path': settings['static_path']}),
        ],
        **settings)


if __name__ == "__main__":
    translator = GlosbeTranslator()

    app = panki_app(translator, "ru", "de")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
