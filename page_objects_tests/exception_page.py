from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects_tests.base_page import BasePage


class ExceptionPage(BasePage):

    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __row_1_field = (By.XPATH, "//div[@id='row1']/input")
    __row_1_save_btn = (By.XPATH, "//button[@id='save_btn']")
    __row_2_field = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")
    __row_2_save_btn = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']")
    __confirmation_msg = (By.ID, "confirmation")
    __add_btn = (By.ID, "add_btn")
    __edit_btn = (By.XPATH, "//button[@id='edit_btn']")
    __instruction = (By.XPATH, "//p[@id='instructions']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_btn)
        super()._wait_until_element_is_visible(self.__row_2_field)

    def is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__row_2_field)

    def add_input_in_row2(self, food: str):
        super()._type(self.__row_2_field, food)
        super()._click(self.__row_2_save_btn)
        super()._wait_until_element_is_visible(self.__confirmation_msg)

    def get_confirmation_msg(self) -> str:
        return super()._get_text(self.__confirmation_msg)

    def modify_row1_field(self, food: str):
        super()._click(self.__edit_btn)
        super()._find(self.__row_1_field)
        super()._wait_until_element_is_clickable(self.__row_1_field)
        super()._clear(self.__row_1_field)
        super()._type(self.__row_1_field, food)
        super()._click(self.__row_1_save_btn)
        super()._wait_until_element_is_visible(self.__confirmation_msg)

    def instruction_msg(self) -> str:
        super()._wait_until_element_is_visible(self.__instruction)
        super()._click(self.__add_btn)
        super()._wait_until_element_is_invisible(self.__instruction)
