#!coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTrc:
    logo = (By.CLASS_NAME, "web_logo")

    def testa(self):
        chromedriver = r"E:\workspace\repo\selenium\chromedriver\ChromeDriver 76.0.3809.126.exe"
        driver = webdriver.Chrome(chromedriver)
        driver.get("https://www.trc.com")
        ele = driver.find_element(*self.logo)
        print(ele)
        ele.click()
        driver.quit()
