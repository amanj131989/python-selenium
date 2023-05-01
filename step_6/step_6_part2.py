# SetUp & Teardown example
# Class & Module fixture means methods that called before and after the 
import unittest
import HtmlTestRunner

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Do a expensive initialization operation here, that should be done once
        print("In SetUp Class")

    def setUp(self):
        # a setup method before every testcase
        print("In test setup method")
     
      # individual tests starts with test
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # More details https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures
    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    def teardown(self):
        # a setup method before every testcase
        print("In test teardown method")
        
    @classmethod
    def tearDownClass(cls):
        # Do test cleanup here, that should be done once
        print("In tearDown Class")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    
