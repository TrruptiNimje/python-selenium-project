import time

import selenium
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    def test_negative_username(self):
        # Open Browser
        driver = selenium.webdriver.Chrome()

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
