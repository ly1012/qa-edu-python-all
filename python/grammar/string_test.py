import pytest

"""
测试对象：   字符串
"""
class TestString():

    """
    测试对象：    string.format
    测试点：       1. 格式化
                  2. {} 转义
    """
    def test_format_param(self):
        name = "liyun"                  # 参数：姓名
        first_name = "yun"              # 参数：名
        last_name = "li"                # 参数：姓
        # 格式化
        assert "My name is {}".format(name) == "My name is liyun"
        # {} 转义：双写大括号，即 {{ 表示 { 本身，}} 表示 } 本身。
        assert "My name is {{{}{}}}".format(last_name, first_name) == "My name is {liyun}"

