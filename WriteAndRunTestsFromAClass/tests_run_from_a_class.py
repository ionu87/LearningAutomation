import pytest
from WriteAndRunTestsFromAClass.class_to_test import SomeClassToTests

# Add all fixtures w want to use here instead of adding them as parameters to the functions
# Now this fixtures are available for all methods under the TestClassDemo
@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class TestClassDemo():
    # Create a fixture for the test_methodA and test_methodB to act as a common object
    # autouse=True makes the fixture available for all methods in the class
    @pytest.fixture(autouse=True)
    def classSteup(self):
        self.abac = SomeClassToTests(10)

    def test_methodA(self):
        result = self.abac.sumNumbers(2, 8)
        #assert only appears in the test result is it fails
        assert result == 20
        print("Running  method A")

    def test_methodB(self):
        print("Running  method B")