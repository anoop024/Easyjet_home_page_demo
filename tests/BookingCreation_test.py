from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import keyboard
import time
from pages.Home_page import Home_Page

driver = webdriver.Chrome(executable_path= r"..\drivers\chromedriver.exe")
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("https://www.easyjet.com/en/")
flight_search = Home_Page(driver)
# flight_search.sign_in("anoop.gupta@easyjet.com","password")
flight_search.onewayflight("yes")
flight_search.routeselection("ltn", "edi")
flight_search.departuredate("2020-08-26")
flight_search.arrivaldate("2020-08-29")
flight_search.noofadultpax(1)
flight_search.noofchildpax(1)
flight_search.noofinfantpax(1)
flight_search.show_flight()
time.sleep(5)
print("successful")
print(driver.title)
driver.close()
driver.quit()