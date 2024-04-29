import time

import pytest
from selenium.webdriver.common.by import By

from page_objects_tests.login_page import LoginPage


class TestNegativeLoginScenario:
    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_username(self, driver, username, password, expected_error_message):

        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_msg() == expected_error_message, "Error message is not expected"
