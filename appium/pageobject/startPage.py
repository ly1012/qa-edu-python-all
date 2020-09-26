from common.BasePage import BasePage
from selenium.webdriver.common.by import By

class StartPage(BasePage):
    # 定位元素
    lijitiyan = (By.CLASS_NAME,"android.widget.Button")

    def click_lijitiyan(self):
        self.find_element(*self.lijitiyan).click()
