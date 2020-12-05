import unittest


class TestCaseDemo(unittest.TestCase):
    # Works like a precondition to a test. We can create test data etc
    def setUp(self):
        print('I will run once before every test')

    def test_case1(self):
        print('Running method 1')

    def test_case2(self):
        print('Running method 2')

    # Cleans up all the data creating during the test execution. If you don't want to clear the data don't use this method
    def tearDown(self):
        print('I will run after every test')

if __name__ == '__main__':
    unittest.main(verbosity=2)