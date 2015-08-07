__author__ = 'wenzou'
import unittest
from objects import CreditManager

class TestCreditManager(unittest.TestCase):

    def setUp(self):
        self.creditManager = CreditManager()

    def test_one_guid(self):
        credits = self.creditManager.return_credits(['tag:wiredrive,2011-03-18:token:128b053b916ea1f7f20233e8a26bc45d:21239'])
        self.assertTrue('MTV Choose or Lose' in credits)
        self.assertTrue('Bryan Buckely' in credits)
        self.assertTrue('J Walter Thompson / New York' in credits)
        self.assertTrue('Hungryman' in credits)
        self.assertTrue('Cannes Gold Lion 2009' in credits)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
