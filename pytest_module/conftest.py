import pytest

# Generic method used in the test_conftest_demo1 and test_conftest_demo2 test cases to run before and after every test case
@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp(browser, osType):
    print("Running conftest demo one time setUp")
    if browser == 'firefox':
        print('Runninf tests on firefox')
    # If i don't provide the browser time it will run by default on Chrome
    else:
        print('Running tests on Chrome')
    yield
    print("Running conftest demo one time tearDown")


# Run test on different browsers or operating systems
def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='Type or operating system')


# Create also fixtures for this
@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')