import unittest
import xmlrunner
import os, sys, inspect
from src.resources import app

class UnitTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def testIndex(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
