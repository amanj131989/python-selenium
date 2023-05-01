# Unittest in python
# The unittest unit testing framework
#  It supports test automation, sharing of setup and shutdown code for tests, 
# aggregation of tests into collections, and independence of the tests from the reporting framework.

# Terminology:
# test case: A test case is the individual unit of testing
# test suite: A test suite is a collection of test cases, test suites, or both executed together
# test runner: A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.


# Example: test three string methods:
import unittest

# A testcase is created by subclassing unittest.TestCase
class TestStringMethods(unittest.TestCase):

  # individual tests starts with test
  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
  unittest.main()
  
# Ways to run in a command line
# $ python -m unittest test_module1 test_module2
# $ python -m unittest step_6

# $ python -m unittest test_module.TestClass
# $ python -m unittest step_6.TestStringMethods

# $ python -m unittest test_module.TestClass.test_method
# $ python -m unittest step_6.TestStringMethods.test_split

# Can also be called through a file directly 
# $ python -m unittest tests/test_something.py

# When executed without arguments Test Discovery is started:
# https://docs.python.org/3/library/unittest.html#unittest-test-discovery
# python -m unittest


