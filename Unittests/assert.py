import unittest


class Assert(unittest.TestCase):

    def test_AssertTrueFalse(self):
        a = True
        self.assertTrue(a, 'a is not false')
        b = False
        self.assertFalse(b, 'b is not true')

    def test_AssertEqual(self):
        a = 'test'
        b = 'test1'
        self.assertNotEqual(a, b, msg='a does not equal to b')


if __name__ == '__main__':
    unittest.main(verbosity=2)