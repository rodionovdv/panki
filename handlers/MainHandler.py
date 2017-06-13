import tornado.web
from tornado.template import Loader

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = Loader("./templates")
        #print(loader.load("base.html"))
        self.write(loader.load("base.html").generate())


    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote new " + self.get_body_argument("message"))
