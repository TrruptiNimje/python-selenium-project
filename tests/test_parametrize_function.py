import time

import pytest
from selenium.webdriver.common.by import By


class TestParametrizeLoginScenario:
    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_username(self, driver, username, password, expected_error_message):

        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        time.sleep(2)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)
        time.sleep(2)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_msg_display = driver.find_element(By.ID, "error")
        assert error_msg_display.is_displayed(), "Error message is not displayed as it should"
        time.sleep(2)

        # Verify error message text is Your username is invalid!
        error_msg = error_msg_display.text
        assert error_msg == expected_error_message, "Error message is not expected"
        time.sleep(2)



