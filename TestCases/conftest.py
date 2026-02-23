import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Ie()

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##### PyTest HTML Report #####

def pytest_metadata(metadata):
    metadata['Project Name'] = 'My Home Entry'
    metadata['Module Name'] = 'Dashboard'
    metadata['Tester Name'] = 'My Tester'

