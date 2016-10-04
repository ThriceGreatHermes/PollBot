class HandlerManager(object):
    def __init__(self, slack_client):
        self.slack_client = slack_client
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def on_message(self, message):
        for handler in self.handlers:
            handler.handle(self.slack_client, message)


class KeywordHandler(object):
    def __init__(self, keyword, callback):
        self.keyword = keyword
        self.callback = callback

    def handle(self, slack_client, message):
        if self.keyword in message.get('text'):
            self.callback(slack_client, message)