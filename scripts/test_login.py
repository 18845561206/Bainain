import time

from base.base_action import BaseAction
from base.base_driver import init_driver


class Test_Login():
    def setup(self):
        self.driver = init_driver()
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    def test_login(self):
        print("Hello World!")
