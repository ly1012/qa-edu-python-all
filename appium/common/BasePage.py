from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, caps):
        self.driver = driver
        self.caps = caps

    def get_size(self):
        """
        获取窗口大小
        :return: size
        """
        return self.driver.get_window_size()

    def get_window_width(self):
        """
        获取窗口宽度
        :return: width
        """
        size = self.get_size()
        return size['width']

    def get_window_height(self):
        """
        获取窗口高度
        :return: height
        """
        size = self.get_size()
        return size['height']

    def find_element(self, *loc):
        """
        元素定位
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(loc))
            return self.find_element(*loc)
        except:
            print('%s 未找到元素 %s', self, loc)
