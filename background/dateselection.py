import keyboard
import time

class dateselection():

    def __init__(self, driver):
        self.driver = driver
        self.driver.date_14_august = "//span[@class='sign-in']"


    def departure_date_selection(self):
        self.driver.find_element_by_xpath(self.driver.date_14_august).click()


    def arrival_date_selection(self):
        self.driver.find_element_by_css_selector(self.driver.arrivaldate_button_css_selector).click()
