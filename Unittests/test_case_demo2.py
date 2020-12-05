import unittest


class TestCaseDemo(unittest.TestCase):
    # Works like a precondition to a test case. We can create test data etc and it will run once for all methods
    @classmethod
    def setUpClass(cls):
        print('*' * 30)
        print('I will run only once before all tests')
        print('*' * 30)

    def setUp(self):
        print('I will run once before every test')

    def test_case1(self):
        print('Running method 1')

    def test_case2(self):
        print('Running method 2')

    # Cleans up all the data creating during the test case execution. If you don't want to clear the data don't use this method
    def tearDown(self):
        print('I will run after every test')

    @classmethod
    def tearDownClass(cls):
        print('*' * 30)
        print('I will run only once after all test methods have been run in the class')
        print('*' * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)