import time

import pytest
import selenium


@pytest.fixture(params=["chrome", "safari"])
def driver(request):

    # browser = request.config.getoption("--browser") >> enable this for command-line execution

    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = selenium.webdriver.Chrome()
        time.sleep(2)
    elif browser == "safari":
        my_driver = selenium.webdriver.Safari()
        time.sleep(2)
    else:
        raise TypeError(f"Expected 'chrome' or 'safari', but git {browser}")
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