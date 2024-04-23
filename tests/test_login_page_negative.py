import time

import pytest
import selenium
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.negativetest
    @pytest.mark.login
    def test_negative_username(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_msg_display = driver.find_element(By.ID, "error")
        assert error_msg_display.is_displayed(), "Error message is not displayed as it should"

        # Verify error message text is Your username is invalid!
        error_msg = error_msg_display.text
        assert error_msg == "Your username is invalid!", "Error message is not expected"

    @pytest.mark.negativetest
    @pytest.mark.login
    def test_negative_password(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_msg_display = driver.find_element(By.ID, "error")
        assert error_msg_display.is_displayed(), "Error message is not displayed as it should"

        # Verify error message text is Your password is invalid!
        error_msg = error_msg_display.text
        assert error_msg == "Your password is invalid!", "Error message is not expected"
