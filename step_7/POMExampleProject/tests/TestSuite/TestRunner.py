from unittest import TestLoader, TestSuite, TextTestRunner
from tests.Scripts.test_web_form import WebFormTestCase
from tests.Scripts.test_submit_page import SubmitTestCase
from HtmlTestRunner import HTMLTestRunner


if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(WebFormTestCase),
        test_loader.loadTestsFromTestCase(SubmitTestCase),
    ))

    test_runner = TextTestRunner(verbosity=2)
    # test_runner = HTMLTestRunner(output='example_suite')
    # runner.run(test_suite)
    
    test_runner.run(test_suite)

