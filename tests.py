__author__ = 'wenzou'
import unittest
from objects import CreditManager

class TestCreditManager(unittest.TestCase):

    def setUp(self):
        self.creditManager = CreditManager()
        self.local_xml_file = 'file://localhost/Users/wenzou/PycharmProjects/developer_test/test_data/testdata1000000.xml'

    def test_no_guid(self):
        credits = self.creditManager.return_credits([])
        self.assertEqual(credits, [])
    def test_bad_guid(self):
        credits = self.creditManager.return_credits(['XYDI'])
        self.assertEqual(credits, [])

    def test_one_guid(self):
        credits = self.creditManager.return_credits(['tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21239'])
        self.assertTrue('MTV Choose or Lose' in credits)
        self.assertTrue('Bryan Buckely' in credits)
        self.assertTrue('J Walter Thompson / New York' in credits)
        self.assertTrue('Hungryman' in credits)
        self.assertTrue('Cannes Gold Lion 2009' in credits)

    def test_multiple_guid(self):
        credits = self.creditManager.return_credits(['tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21239',
                                                     'tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21248'])
        self.assertTrue('MTV Choose or Lose' in credits)
        self.assertTrue('Bryan Buckely' in credits)
        self.assertTrue('J Walter Thompson / New York' in credits)
        self.assertTrue('Hungryman' in credits)
        self.assertTrue('Cannes Gold Lion 2009' in credits)
        self.assertTrue('Pizza Pops' in credits)
        self.assertTrue('Scott Corbett' in credits)
        self.assertTrue('Holiday Films' in credits)
        self.assertTrue('Cannes Silver Lion 2009' in credits)

    def test_no_credit(self):
        guids = self.creditManager.return_guids([])
        self.assertEqual(guids, [])

    def test_bad_credit(self):
        guids = self.creditManager.return_guids(['XYDI'])
        self.assertEqual(guids, [])

    def test_one_credit(self):
        guids = self.creditManager.return_guids(['Pizza Pops'])
        self.assertEqual(guids, ['tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21248',
                                 'tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21249'])

    def test_two_credits(self):
        guids = self.creditManager.return_guids(['Pizza Pops', 'Sticks & Stones'])
        self.assertEqual(guids, ['tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21248',
                                 'tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21249',
                                 'tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21253'])
    """
    def test_local_data_one_guid(self):
        self.creditManager = CreditManager(rss_feed_url=self.local_xml_file)
        credits = self.creditManager.return_credits(['id_1'])
        self.assertTrue('id_1Some Name1' in credits)
    """
    def test_local_data_one_credit(self):
        self.creditManager = CreditManager(rss_feed_url=self.local_xml_file)
        guids = self.creditManager.return_guids(['id_1Some Name1'])
        self.assertTrue('id_1' in guids)

if __name__ == '__main__':
    unittest.main()
