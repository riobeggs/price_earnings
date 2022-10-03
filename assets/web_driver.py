from selenium import webdriver

URL = "https://finance.yahoo.com/most-active"


def run_web_driver():
    driver = webdriver.Chrome(executable_path="/Users/riobeggs/Documents/chromedriver-2")
    driver.get(URL)
    driver.implicitly_wait(5)
    return driver
