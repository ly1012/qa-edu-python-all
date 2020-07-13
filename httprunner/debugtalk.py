"""
@date 2020-04-30
@author LiYun
"""

import requests


def teardown_demo(response: requests.Response):
    print("teardown_hooks.teardown_demo info: ", response.status_code)