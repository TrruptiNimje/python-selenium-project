import pytest

from page_objects_tests.exception_page import ExceptionPage


class TestException:
    @pytest.mark.exception1
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):

        exceptions_page = ExceptionPage(driver)
        exceptions_page.open_page()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 should be displayed, but its not"

    @pytest.mark.exception2
    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):

        exceptions_page = ExceptionPage(driver)
        exceptions_page.open_page()
        exceptions_page.add_second_row()
        exceptions_page.add_input_in_row2("Sushi")
        assert exceptions_page.get_confirmation_msg() == "Row 2 was saved", "Save message is not as expected"

    @pytest.mark.exception3
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):

        exceptions_page = ExceptionPage(driver)
        exceptions_page.open_page()
        exceptions_page.modify_row1_field("Sushi")
        assert exceptions_page.get_confirmation_msg() == "Row 1 was saved", "Save message is not as expected"

    @pytest.mark.exceptions
    @pytest.mark.exception4
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionPage(driver)
        exceptions_page.open_page()
        exceptions_page.instruction_msg()

    @pytest.mark.exceptions
    @pytest.mark.exception5
    def test_timeout_exception(self, driver):

        exceptions_page = ExceptionPage(driver)
        exceptions_page.open_page()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 should be displayed, but its not"
