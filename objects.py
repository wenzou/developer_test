__author__ = 'wenzou'
import urllib2
from xml.etree import ElementTree as etree

class CreditManager:
    'manages the media content credits'
    rss_feed_url = 'http://www.wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d'

    def __init__(self, rss_feed_url=None):
        print 'credit Manager created'
        #feed parse
        self.rss_feed_url = rss_feed_url if rss_feed_url else self.rss_feed_url
        feed_file = urllib2.urlopen(self.rss_feed_url)
        #convert to string:
        feed_data = feed_file.read()
        #print feed_data
        #close file because we dont need it anymore:
        feed_file.close()

        #entire feed
        self.data_root = etree.fromstring(feed_data)

    def return_credits(self, guids):
        item = self.data_root.findall(".//*[guid='" + guids[0] + "']")
        credits = item[0].findall(".//{http://search.yahoo.com/mrss/}credit")
        creditList = []
        for credit in credits:
            creditList.append(credit.text)
        return creditList

