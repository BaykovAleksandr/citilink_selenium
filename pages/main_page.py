import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    url = 'https://citilink.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_icon_locator = '''//*[@id="__next"]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span'''
    user_name_locator = '''/html/body/div[9]/div/div/div/div/div[2]/div/div/div/form/div/div/div[1]/div/
    div/label/input'''
    password_locator = '''/html/body/div[9]/div/div/div/div/div[2]/div/div/div/form/div/div/div[2]/div/label/input'''
    submit_button_locator = '''/html/body/div[9]/div/div/div/div/div[2]/div/div/div/form/div/button'''

    catalog = "//button[@data-label='Каталог товаров']"
    select_category = '''/html/body/div[2]/div[2]/header
    /div[3]/div/div/div/div/div/menu/div/div[2]/div[2]/div[1]/div[2]/a/span'''

    # Getters
    def get_login_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_icon_locator)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button_locator)))

    def get_select_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category)))

    # Actions

    def click_login_icon(self):
        self.get_login_icon().click()
        print("Click login button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input login")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")

    def click_catalog(self):
        self.get_select_catalog().click()
        print("Select Catalog")

    def click_category(self):
        self.get_select_category().click()
        print("Select Category")

    # Methods

    def select_catalog(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_icon()
        time.sleep(3)
        self.input_user_name("aleksandrnsk12@yandex.ru")
        time.sleep(3)
        self.input_password("DwZ(LLfv9T+_Hw+")
        time.sleep(3)
        self.click_submit_button()
        time.sleep(3)
        self.click_catalog()
        self.click_category()
