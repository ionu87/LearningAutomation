import pytest

# The fixture method runs the PreConfig method before every test method, if given as a paramter to the test method
@pytest.fixture()
def PreConfiguration():
    print('Runs once before every method')

def test_methodA(PreConfiguration):
    print('Run method A')


def test_methodB():
    print('Run method B')