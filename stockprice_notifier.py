import os
import time
import msvcrt
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from smtplib import SMTP
import email


load_dotenv()

url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"

def get_driver():
    """This function creates the webdriver. The following options where recommended in the Udemy Course this project is
    based on, and solve common issues when accessing a browser via selenium"""
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start_maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-Automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    return driver


def clean_text(text: str) -> float:
    """
        Converts the text from the stockprice change into a numerical value.
    :param text:
    :return:
    """

    output = float(text.split(" ")[0])
    return output


def send_email(sp_change: float):
    """
        Sends an E-mail notifying about the stock price change being below 0.1%
    :param sender: e-mail address of the sender
    :param recipient: e-mail address of the recipient
    """
    sender = os.environ["SENDER"]
    receiver = os.environ["RECEIVER"]
    password = os.environ["PASSWORD"]

    # Construct the email
    message = email.message_from_string(f"This message informs you, that the stock price change is currently {sp_change}.")
    message["Subject"] = "The stock price change sank below -0.1%!"
    message["From"] = sender
    message["To"] = receiver

    # send the e-mail via microsoft outlook SMTP server
    s = SMTP("smtp-mail.outlook.com", 587)
    s.ehlo() # initiation of the extended smtp protocol
    s.starttls() # puts connection to SMTP server in TLS mode
    s.login(sender, password) # logs the sender into their mail account
    s.sendmail(sender, receiver, message.as_string())

    print(f"A notification e-mail was sent out to {receiver}!")


def get_stockprice_change():
    driver = get_driver()
    while True:
        # End the loop on keystroke
        if msvcrt.kbhit():
            break
        time.sleep(2)
        element = driver.find_element(By.XPATH, '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
        sp_change = clean_text(element.text)
        if sp_change < -0.1:
            send_email(sp_change)


get_stockprice_change()