import tornado.websocket


class UIHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):

        resp = self.translator.translate(message, self._from, self._to)
        print(resp)
        self.write_message("Response "+str(resp))


    def on_close(self):
        print("WebSocket closed")

    def initialize(self, translator, _from, _to):
        self.translator = translator
        self._from = _from
        self._to = _to
