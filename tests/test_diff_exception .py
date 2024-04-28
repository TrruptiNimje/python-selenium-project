import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


class TestException:

    @pytest.mark.exception1
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        driver.find_element(By.ID, "add_btn").click()

        wait = WebDriverWait(driver, 10)
        # Verify Row 2 input field is displayed

        row_2_input_field_element = wait.until(
            ec.presence_of_element_located(
                (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")))
        assert row_2_input_field_element.is_displayed(), " Row 2 should be displayed but its not "

    @pytest.mark.exception2
    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        driver.find_element(By.ID, "add_btn").click()

        wait = WebDriverWait(driver, 10)
        # Verify Row 2 input field is displayed
        row_2_input_field_element = wait.until(
            ec.presence_of_element_located(
                (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")))
        assert row_2_input_field_element.is_displayed(), " Row 2 should be displayed but its not "

        # Type text into the second input field
        row_2_input_field_element.send_keys("TestData")

        # Push Save button using locator By.name(“Save”)
        """
        Following Name locator will fail the test 
        - driver.find_element(By.NAME, "Save").click()
        But using the following XPath locator will pass test 

        """

        driver.find_element(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']").click()

        # Verify text saved
        saved_msg_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        save_msg = saved_msg_element.text
        assert save_msg == "Row 2 was saved", "Save message is not as expected"

    @pytest.mark.exception3
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        driver.find_element(By.XPATH, "//button[@id='edit_btn']").click()
        row_1_field_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_field_locator))
        row_1_field_locator.clear()

        # Type text into the input field
        row_1_field_locator.send_keys("Sushi")
        driver.find_element(By.XPATH, "//button[@id='save_btn']").click()

        # Verify text changed
        row_1_save_msg = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='confirmation']")))
        save_msg = row_1_save_msg.text
        assert save_msg == "Row 1 was saved", "Save message is not as expected"

    @pytest.mark.exceptions
    @pytest.mark.exception4
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        add_instruction_text = driver.find_element(By.XPATH, "//p[@id='instructions']")
        instruction_msg = add_instruction_text.text
        assert instruction_msg == "Push “Add” button to add another row", "Not expected instruction"

        # Push add button
        driver.find_element(By.ID, "add_btn").click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        wait.until(ec.invisibility_of_element(add_instruction_text))

        """
        The following line will create expected exception if used instead of explicit wait
        assert not add_instruction_text.is_displayed(), "Text is still present"
        """

    @pytest.mark.exceptions
    @pytest.mark.exception5
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        driver.find_element(By.ID, "add_btn").click()

        # Wait for 3 seconds for the second input field to be displayed
        # this should fail as intended timeout is 10sec by default

        wait = WebDriverWait(driver, 10)

        # Verify Row 2 input field is displayed
        row_2_input_field_element = wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")),
            " Row 2 should be displayed but its not ")
