import unittest
from Unittests.test_case_demo1 import TestCaseDemo
from Unittests.test_case_demo2 import TestCaseDemo


# Get all tests from test_case_demo1 and test_case_demo2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)

# Create a test suite  combining test_case_demo1 and test_case_demo2
smoke_test = unittest.TestSuite([tc1, tc2])

# Trigger the run
unittest.TextTestRunner(verbosity=2).run(smoke_test)