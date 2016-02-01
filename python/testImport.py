
import urllib2
from MyHtmlParser import MyHtmlParser

translationMap = ''
for i in range(256):
    if i <= 127:
        translationMap += chr(i)
    else: # Replace high-end ascii characters with '?'
        translationMap += '?'


def HtmlRetriever(url):
    req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib2.urlopen(req)
    return con.read().translate(translationMap)


def main():
    url = "https://www.airbnb.com/careers/departments/business-development"

    html = HtmlRetriever(url)
    print "length of html string:", len(html)

    parser = MyHtmlParser()
    parser.feed(html)
    print "parser links 2: ", parser.links

main()
