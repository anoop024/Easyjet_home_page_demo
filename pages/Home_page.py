from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time
class Home_Page():

    def __init__(self, driver):
        self.driver = driver
        # Sign-in details
        self.driver.SignIn_link_xpath = "//span[@class='sign-in']"
        self.driver.SignInOption_selector_name = "sign-in-option"
        self.driver.emailId_textbox_id = "signin-username"
        self.driver.password_testbox_id = "signin-password"
        self.driver.KeepMesignedIn_checkbox_xpath = "//div[@class='ej-checkbox ej-checkbox-multiline-text ej-text ej-text-dark checked']//span[@class='checkbox']"
        self.driver.SignIn_button_name = "login"
        # Route details
        self.driver.routeselector_checkbox_xpath = "//span[@class='checkbox-label-text']"
        self.driver.depatureairport_textbox_name = "origin"
        self.driver.arrivalairport_textbox_name = "destination"
        # departing date selector
        self.driver.departingdateselector_link_xpath = "//span[contains(text(),'Departing')]"
        self.driver.departuredate_button_css_selector = "div.drawer-outer:nth-child(9) div.drawer.drawer-angular.anim-slide-rtr div.drawer-inner div.anim-slide-rtl.drawer-section-wrapper div.drawer-section.routedatepicker div.drawer-scrolling-area.sessioncammonitorscroll div.drawer-content-outer div.drawer-content.notranslate div.route-date-picker-drawer.ej-text.ej-text-dark div.drawer-tab-content-wrapper div.drawer-tab-content.active:nth-child(1) div:nth-child(1) div.month div.route-date-picker-month div.calendar-month div.day"
        self.driver.departing_button_xpath = "//div[@class='tab-button-wrapper active']"
        # Returning date selector
        self.driver.Returningdateselector_link_id = "routedatepicker-30824"
        self.driver.returningdate_button_css_selector = "div.drawer-outer:nth-child(9) div.drawer.drawer-angular.anim-slide-rtr div.drawer-inner div.anim-slide-rtl.drawer-section-wrapper div.drawer-section.routedatepicker div.drawer-scrolling-area.sessioncammonitorscroll div.drawer-content-outer div.drawer-content.notranslate div.route-date-picker-drawer.ej-text.ej-text-dark div.drawer-tab-content-wrapper div.drawer-tab-content.active:nth-child(2) div:nth-child(1) div.month div.route-date-picker-month div.calendar-month div.day"
        self.driver.returning_button_xpath = "//button[contains(text(),'Returning')]"
        # adult pax
        self.driver.countofadultpax_text_xpath = "//input[@id='Adults-175811']"
        self.driver.addadultpax_button_xpath = "//div[@class='search-passengers-adults search-row']//button[@class='quantity-button-add']//img[1]"
        self.driver.removeadultpax_button_xpath = "//div[@class='search-passengers-adults search-row']//button[@class='quantity-button-remove']//img[1]"
        # child pax
        self.driver.addchildpax_button_xpath = "//div[@class='search-passengers-children search-row']//button[@class='quantity-button-add']//img[1]"
        self.driver.removechildpax_button_xpath = "//div[@class='search-passengers-children search-row']//button[@class='quantity-button-remove']//img[1]"
        self.driver.flyingwithoutadult_button_css_selector = "div.drawer-outer:nth-child(9) div.drawer.drawer-angular.anim-slide-rtr div.drawer-inner div.anim-slide-rtl.drawer-section-wrapper div.drawer-section.too-many-children-travelling-alone div.header-wrapper div.drawer-header.notranslate div.close-drawer-button button.ej-link-button > img:nth-child(1)"
        self.driver.flyingwithoutadult_text_css_selector = "div.drawer-outer:nth-child(9) div.drawer.drawer-angular.anim-slide-rtr div.drawer-inner div.anim-slide-rtl.drawer-section-wrapper div.drawer-section.too-many-children-travelling-alone div.drawer-scrolling-area.sessioncammonitorscroll div.drawer-content-outer div.drawer-content.notranslate div:nth-child(1) div.message-drawer.ej-text.ej-text-dark:nth-child(2) > div.message-summary"
        # infant pax
        self.driver.addinfantpax_button_xpath = "//div[@class='search-passengers-infants search-row']//button[@class='quantity-button-add']//img[1]"
        self.driver.removeinfantpax_button_xpath = "//div[@class='search-passengers-infants search-row']//button[@class='quantity-button-remove']//img[1]"
        # flight search button
        self.driver.showflight_button_xpath = "//button[@class='ej-button rounded-corners arrow-button search-submit']"
        # infant information drawer - continue button
        self.driver.continuedrawerforinfant_button_css_selector = "div.drawer-outer:nth-child(9) div.drawer.drawer-angular.anim-slide-rtr div.drawer-inner div.anim-slide-rtl.drawer-section-wrapper div.drawer-section.search-with-infants div.drawer-scrolling-area.sessioncammonitorscroll div.drawer-content-outer.has-back div.drawer-content.notranslate div:nth-child(1) div.message-drawer.ej-text.ej-text-dark:nth-child(2) > div.drawer-button"

    def sign_in(self, email, password):
        self.driver.find_element_by_xpath(self.driver.SignIn_link_xpath).click()
        self.driver.find_element_by_name(self.driver.SignInOption_selector_name).click()
        self.driver.find_element_by_id(self.driver.emailId_textbox_id).send_keys(email)
        self.driver.find_element_by_id(self.driver.password_testbox_id).send_keys(password)
        # self.driver.find_element_by_xpath(self.driver.KeepMesignedIn_checkbox_xpath).click()
        self.driver.find_element_by_name(self.driver.SignIn_button_name).click()

    def onewayflight(self, value1):
        global one_way
        if value1 == "yes":
            self.driver.find_element_by_xpath(self.driver.routeselector_checkbox_xpath).click()
        one_way = value1

    def routeselection(self, departure, arrival):
        self.driver.find_element_by_name(self.driver.depatureairport_textbox_name).click()
        self.driver.find_element_by_name(self.driver.depatureairport_textbox_name).clear()
        self.driver.find_element_by_name(self.driver.depatureairport_textbox_name).send_keys(departure)
        keyboard.press('Tab')
        self.driver.find_element_by_name(self.driver.arrivalairport_textbox_name).send_keys(arrival)
        keyboard.press('Tab')

    def departuredate(self, departure_date):
        self.driver.find_element_by_xpath(self.driver.departingdateselector_link_xpath).click()
        try:
            calendar_block = self.driver.find_element_by_xpath(self.driver.departing_button_xpath).click()
            keyboard.press('Tab')
            keyboard.press('Tab')
            keyboard.press('Tab')
            date_picker = self.driver.find_elements_by_css_selector(self.driver.departuredate_button_css_selector)
            for days in date_picker:
                day = days.get_attribute("data-date")
                if day == departure_date:
                    days.click()
                    break
                keyboard.press('Tab')
        except:
            print("Departure date is Invalid")


    def arrivaldate(self, returning_date):
        if one_way == "yes":
            return
        else:
            try:
                self.driver.find_element_by_xpath(self.driver.returning_button_xpath).click()
                keyboard.press('Tab')
                keyboard.press('Tab')
                date_picker_return = self.driver.find_elements_by_css_selector(
                    self.driver.returningdate_button_css_selector)
                for days in date_picker_return:
                    day = days.get_attribute("data-date")
                    if day == returning_date:
                        days.click()
                        break
                    keyboard.press('Tab')
            except:
                print("Returning date is invalid")


    def noofadultpax(self, number):
        global no_of_adultpax
        global no_of_childpax
        no_of_adultpax = number
        if no_of_adultpax != 0:
            for i in range(no_of_adultpax - 1):
                self.driver.find_element_by_xpath(self.driver.addadultpax_button_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.driver.addchildpax_button_xpath).click()
            time.sleep(1)
            self.driver.find_element_by_xpath(self.driver.removeadultpax_button_xpath).click()
            time.sleep(2)
            Flying_without_adults = self.driver.find_element_by_css_selector(self.driver.flyingwithoutadult_text_css_selector)
            print(Flying_without_adults.text)
            self.driver.find_element_by_css_selector(self.driver.flyingwithoutadult_button_css_selector).click()


    def noofchildpax(self, number):
        no_of_childpax = number
        if no_of_childpax < (no_of_adultpax * 10):
            if no_of_adultpax != 0:
                for i in range(no_of_childpax):
                    self.driver.find_element_by_xpath(self.driver.addchildpax_button_xpath).click()
            else:
                return
        else:
            print("No more than 10 children may travel per adult on a booking")

    def noofinfantpax(self, number):
        global no_of_infants
        no_of_infants = number
        if no_of_infants <= no_of_adultpax:
            for i in range(no_of_infants):
                self.driver.find_element_by_xpath(self.driver.addinfantpax_button_xpath).click()
        else:
            print("Only one infant per adult is allowed")

    def show_flight(self):
        self.driver.find_element_by_xpath(self.driver.showflight_button_xpath).click()
        if no_of_infants != 0:
            try:
                self.driver.implicitly_wait(10)
                continue_button = self.driver.find_element_by_css_selector(self.driver.continuedrawerforinfant_button_css_selector)
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, continue_button))
                element.click()
            except:
                print("Data is insufficient or wrong")















