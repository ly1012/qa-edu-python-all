# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from common.swip_util import SwipUtil
import time
from pageobject.startPage import StartPage


class TestLogin:
    def setup(self):

        self.caps = {}
        self.caps["platformName"] = "android"
        self.caps["deviceName"] = "trc"
        self.caps["automationName"] = "uiautomator2"
        self.caps["appPackage"] = "com.tairanchina.taiheapp"
        self.caps["appActivity"] = "com.tairanchina.taiheapp.module.finance.activity.LaunchActivity"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        self.driver.implicitly_wait(10)


    def test_loin(self):

        # 鼠标向左滑动
        swipUtil = SwipUtil(self.driver,self.caps)
        swipUtil.swip_left()
        time.sleep(1)
        swipUtil.swip_left()
        time.sleep(1)
        # 点击立即体验按钮
        # startPage = StartPage(self.driver,self.caps)
        # startPage.click_lijitiyan()
        self.driver.find_element_by_class_name("android.widget.Button").click()
        # 关闭广告弹窗
        self.driver.find_element_by_id("activityLayerClose").click()


        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.Button").click()
        # time.sleep(1)
        # #关掉弹窗
        # self.driver.find_element_by_id("activityLayerClose")
        # # 点击我的
        # self.driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="trcShoppingTag"]/android.widget.TextView')
        # # 点击登录
        # el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
        # el1.click()
        # el2 = self.driver.find_element_by_id("com.tairanchina.taiheapp:id/accountLoginPwPhone")
        # el2.send_keys("15036537071")
        # el3 = self.driver.find_element_by_id("com.tairanchina.taiheapp:id/accountLoginPwPw")
        # el3.send_keys("qqq111")
        # el4 = self.driver.find_element_by_id("com.tairanchina.taiheapp:id/accountLoginPwSubmit")
        # el4.click()

