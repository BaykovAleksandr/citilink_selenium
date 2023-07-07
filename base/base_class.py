import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url: {get_url}')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert price"""

    def assert_price(self, price, result):
        value_price = price.text
        assert value_price == result
        print("Good value price")

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y, %m, %d, %H, %M, %S")
        name_screenshot = f'screenshot{now_date}.png'
        self.driver.save_screenshot(r'C:\Users\1\pythonProject\sitilink\screen' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
