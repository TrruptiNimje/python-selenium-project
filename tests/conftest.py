import pytest
import selenium
from selenium import webdriver


# @pytest.fixture(params=["chrome", "safari"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = selenium.webdriver.Chrome()
    elif browser == "safari":
        my_driver = selenium.webdriver.Safari()
    else:
        raise TypeError(f"Expected 'chrome' or 'safari', but git {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or safari)"
    )


"""
    "--browser", action="store",  ****"
    This code line is for commandline test execution.
    example of how to run from commandline: 
    'pytest --browser safari test_name'
"""