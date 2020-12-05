import pytest

''' The yeld_fixture decorator method runs the PreConfiguraiton method before and after every test method, 
if given as a parameter
'''
@pytest.fixture()
def PreConfiguration():
    print('Runs once before every method')
    yield
    print('Runs once after every method')

def test_methodA(PreConfiguration):
    print('Run method AA')


def test_methodB(PreConfiguration):
    print('Run method BB')