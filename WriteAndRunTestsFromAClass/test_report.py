import pytest
from WriteAndRunTestsFromAClass.class_to_test import SomeClassToTests

@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class TestClassDemo():
    @pytest.fixture(autouse=True)
    def classSteup(self):
        self.abac = SomeClassToTests(10)

    def test_methodA(self):
        result = self.abac.sumNumbers(2, 8)
        assert result == 20
        print("Running  method A")

    def test_methodB(self):
        result = self.abac.sumNumbers(2, 8)
        assert result > 20
        print("Running  method B")