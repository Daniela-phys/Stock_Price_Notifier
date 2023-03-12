from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"


def get_driver():
    """This function creates the webdriver. The following options where recommended in the Udemy Course this project is
    based on, and solve common issues when accessing a brother via selenium"""
    options = webdriver.EdgeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start_maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-Automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Edge(options=options)
    driver.get(url)

    return driver


def clean_text(text: str) -> float:
    """Converts the text from the stockprice change into a numerical value"""
    output = float(text.split(" ")[0])
    return output


def get_stockprice_change():
    driver = get_driver()
    while True:
        # The program stops when the user enters q into the terminal
        if input() == "q":
            break
        time.sleep(2)
        element = driver.find_element(By.XPATH, '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
        sp_change = clean_text(element.text)
        print(sp_change)









get_stockprice_change()