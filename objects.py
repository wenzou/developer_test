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

        #create a tree from the entire feed data
        self.data_root = etree.fromstring(feed_data)

    def return_credits(self, guids):
        input_key = 'guid'
        return_key = './/{http://search.yahoo.com/mrss/}credit'
        return self.return_elements(guids, input_key, return_key)

    def return_guids(self, credits):
        input_key = '{http://search.yahoo.com/mrss/}credit'
        return_key = './/guid'
        return self.return_elements(credits, input_key, return_key)

    def return_elements(self, inputs, input_key=None, return_key=None):
        returnList = []
        try:
            #for each credits input
            for input in inputs:
                #find all elements based on the input key
                inputElements = self.data_root.findall(".//*["+input_key+"='" + input + "']")
                #for all input elements
                for inputElement in inputElements:
                    #find return elements based on the input elements.
                    returnElements = inputElement.findall(return_key)
                    for returnElement in returnElements:
                        #collect all the return elements.
                        returnList.append(returnElement.text)
        except Exception:
            pass
        return returnList

