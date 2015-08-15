__author__ = 'wenzou'
import urllib2
from xml.etree import ElementTree as etree
import xml.etree.cElementTree as ET
from xml.etree.cElementTree import iterparse
class CreditManager:
    'manages the media content credits'
    rss_feed_url = 'http://www.wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d'

    def __init__(self, rss_feed_url=None):
        print 'credit Manager created'
        self.rss_feed_url = rss_feed_url if rss_feed_url else self.rss_feed_url

        #feed parse
        tree = ET.ElementTree(file=urllib2.urlopen(self.rss_feed_url))

        #create a tree from the entire feed data
        self.data_root = tree.getroot()


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

class FasterCreditManager:
    'manages the media content credits'
    rss_feed_url = 'http://www.wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d'

    def __init__(self, rss_feed_url=None):
        print 'credit Manager created'
        self.rss_feed_url = rss_feed_url if rss_feed_url else self.rss_feed_url
        self.source= urllib2.urlopen(self.rss_feed_url)
    def return_credits(self, guids):
        input_key = 'guid'
        return_key = '{http://search.yahoo.com/mrss/}credit'
        # get an iterable
        context = iterparse(self.source, events=("start", "end"))

        # turn it into an iterator
        context = iter(context)

        # get the root element
        event, root = context.next()
        correct_guid = False
        items_to_return = []
        for event, elem in context:
            if guids == [] and not correct_guid:
                #all guids have been found
                break
            if event == "end" and elem.tag == input_key and elem.text in guids:
                correct_guid = True
                #pop item from guids list
                guids.pop(guids.index(elem.text))
                root.clear()
            elif event == "end" and elem.tag == input_key and elem.text not in guids:
                correct_guid = False
            elif event == "end" and correct_guid and elem.tag == return_key:
                items_to_return.append(elem.text)
        return items_to_return

    def return_guids(self, credits):
        input_key = '{http://search.yahoo.com/mrss/}credit'
        return_key = 'guid'
        # get an iterable
        context = iterparse(self.source, events=("start", "end"))

        # turn it into an iterator
        context = iter(context)

        # get the root element
        event, root = context.next()
        current_guid = ''
        items_to_return = []
        credits_found = 0
        #if there is no credits in the input, return empty list.
        if len(credits) == 0:
            return items_to_return
        for event, elem in context:
            if len(credits) == credits_found:
                #if the credits found is the same as the credits input, the reutrn the current guid
                if len(items_to_return) == 0:
                    items_to_return.append(current_guid)
                #break
            if event == "end" and elem.tag == return_key:
                #if we found a guid, then set the current guid
                current_guid = elem.text
                #reset the credits_found
                credits_found = 0
            elif event == "end" and elem.tag == input_key and elem.text in credits:
                credits_found+= 1
            root.clear()


        return items_to_return
