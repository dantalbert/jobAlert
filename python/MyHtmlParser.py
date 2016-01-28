
from HTMLParser import HTMLParser


class MyHtmlParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.links = ["test string"]
            # print self.links

        def handle_data(self, data):
            if data == "Head of Business Travel":
                # print data
                self.links.append(data)
                # print self.links
                print self.links.count("Head of Business Travel")
