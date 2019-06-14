import unittest
import xmlrunner
from resources import app

class UnitTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def testIndex(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')

    def testHello(self):
        name = '_yourname_'
        response = self.app.get(f'/hello/{name}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytearray(f'{name}', 'utf-8'), response.data)

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
