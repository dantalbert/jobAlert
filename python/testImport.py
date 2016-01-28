
import urllib2
from MyHtmlParser import MyHtmlParser


def HtmlRetriever(url):
    req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib2.urlopen(req)
    return con.read()


def main():
    url = "https://www.airbnb.com/careers/departments/business-development"

    html = HtmlRetriever(url)

    parser = MyHtmlParser()
    parser.feed(html)
    print parser.links


main()
