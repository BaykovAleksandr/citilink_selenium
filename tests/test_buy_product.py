from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.sub_category_page import SubcategoryPage
from pages.filters_page import FiltersPage
from pages.checkout_page import CheckoutPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def test_buy_product():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    print("Start Test")

    """Выбор категории товара"""

    mp = MainPage(driver)
    mp.select_catalog()

    """Выбор подкатегории товара"""

    pp = SubcategoryPage(driver)
    pp.select_subcategory()

    """Выбор товара по параметрам"""

    fp = FiltersPage(driver)
    fp.select_filters()

    """Переход на страницу оформления товара"""

    op = OrderPage(driver)
    op.registration()

    """Оформление выбраного товара"""

    cp = CheckoutPage(driver)
    cp.checkout()

    print("Finish Tests")
    driver.quit()


