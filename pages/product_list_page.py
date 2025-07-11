import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Product:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def open_product_page(self,url):
        self.driver.get(url)

