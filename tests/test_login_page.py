import pytest

from page_objects_tests.login_page import LoginPage
from page_objects_tests.login_successful_page import LoginSuccessfulPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positivetest
    def test_positive_login(self, driver):
        # Creating instance of page object class to call and use the function
        login_page = LoginPage(driver)

        # Open page
        login_page.open()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login_page.execute_login("student", "Password123")

        # Creating instance of page object class to call and use the function
        logged_in_page = LoginSuccessfulPage(driver)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not same as Expected URL"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in_page.header == "Logged In Successfully", "Header is not as expected"

        # Verify button Log out is displayed on the new page
        assert logged_in_page.is_logout_btn_displayed(), "Logout button not found"

        """
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        log_out_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_locator.is_displayed()
        log_out_locator.click()

        # Close browser
        driver.close()
        """
