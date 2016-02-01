
from HTMLParser import HTMLParser


class MyHtmlParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.links = []

        def handle_data(self, data):
            if data == "Head of Business Travel":
                self.links.append(data)
