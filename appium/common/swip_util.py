from common.BasePage import BasePage


class SwipUtil(BasePage):

    def swip_left(self):
        """
        定义向左滑动方法
        :return:
        """
        width = self.get_window_width()
        x1 = width * 0.8
        x2 = width * 0.1
        y1 = self.get_window_height() * 0.5
        self.driver.swipe(x1, y1, x2, y1)
