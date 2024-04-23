import pytest
import selenium


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = selenium.webdriver.Chrome()
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()
