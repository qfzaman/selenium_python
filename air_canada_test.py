from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=service)

class AirCanadaTest:
    def openHomeScreen(url):
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
    
    def tearDown():
        driver.quit()

    def validateTitle(title):
        actualTitle = driver.title
        if (actualTitle == title):
            print("Pass")
        else:
            print("Fail")

    def navigateToFlightStatus(title):
        element = driver.find_element(By.XPATH, "//div[@class='menu-item']//..//span[text()='Flight status']")
        element.click()
        time.sleep(3)
        actualTitle = driver.title
        if (actualTitle == title):
            print("Pass")
        else:
            print("Fail")

    def closeMainNavigation():
        element = driver.find_element(By.XPATH, "//button[@class='toggle']/span")
        element.click()
        time.sleep(3)

    def findAFlight(flight):
        element = driver.find_element(By.XPATH, "//span[normalize-space()='AC']//..//..//..//div/input")
        element.click()
        element.send_keys(flight)
        element = driver.find_element(By.XPATH, "//button[contains(@class,'abc-button-has-inset-loader')]")
        element.click()
        time.sleep(5)
