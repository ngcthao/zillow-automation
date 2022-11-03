from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

URL = "https://www.zillow.com/new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.47200582910156%2C%22east%22%3A-73.48735617089844%2C%22south%22%3A40.279033988398076%2C%22north%22%3A41.114052531301155%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"


class SelenaBot:
    def __init__(self):
        chrome_driver_path = Service("D:\Development\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=chrome_driver_path, options=op)

    def get_html(self):
        self.driver.get(URL)
        for _ in range(20):
            webdriver.ActionChains(self.driver).key_down(Keys.TAB).perform()
        for _ in range(120):
            webdriver.ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
        html_data = self.driver.page_source
        return html_data

    def input_fields(self, data):
        self.driver.get("https://forms.gle/mK4zkQ89LWRHmYtW6")
        for entry in data:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
            WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions)\
                .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[text()="Submit"]')))

            address_bar = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
            price_bar = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
            link_bar = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
            submit = self.driver.find_element(
                By.XPATH,
                '//span[text()="Submit"]'
            )
            time.sleep(1)
            address_bar.send_keys(entry["address"])
            time.sleep(1)
            price_bar.send_keys(entry["price"])
            time.sleep(1)
            link_bar.send_keys(entry["link"])
            time.sleep(1)
            submit.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[text()="Submit another response"]'))
            )
            new_response = self.driver.find_element(By.XPATH, '//a[text()="Submit another response"]')
            new_response.click()

