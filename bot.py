import sys
import time, selenium
import colorama
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from WebScraper import getItem

def details():
    info = {}
    l = ["Name", "Email", "Phone", "Ad1", "Ad2", "Ad3", "City", "ZIP", "Country", "Card Number", "Card Month", "Card Year", "CVV"]
    i = 0
    while i < 13:
        print(Fore.LIGHTBLUE_EX + l[i] + ": " + Fore.LIGHTGREEN_EX + Style.RESET_ALL)
        info[l[i]] = input()
        i += 1
    return info

def main():
    # Input item info
    print(Fore.MAGENTA + "Choose Category:" + Fore.CYAN + "jackets, shirts, top/sweaters, sweatshirts, pants, shorts, hats, bags, accessories, shoes, skate" + Fore.GREEN)
    category = input()
    print(Fore.MAGENTA + "Item Name: " + Fore.GREEN)
    name = input()
    print(Fore.MAGENTA + "Item Color: " + Fore.GREEN)
    color = input()

    t0 = time.time()
    info = details()

    item = 'https://www.supremenewyork.com' + getItem(category, name, color)
    browser = webdriver.Chrome('/home/mark/Downloads/chromedriver')
    browser.get(item)

    browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    val = True
    while val:
        try:
            browser.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
            val = False
        except:
            continue

    # User info
    browser.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(info["Name"])
    browser.find_element_by_xpath('//*[@id="order_email"]').send_keys(info["Email"])
    browser.find_element_by_xpath('//*[@id="order_tel"]').send_keys(info["Phone"])
    browser.find_element_by_xpath('//*[@id="bo"]').send_keys(info["Ad1"])
    browser.find_element_by_xpath('//*[@id="oba3"]').send_keys(info["Ad2"])
    browser.find_element_by_xpath('//*[@id="order_billing_address_3"]').send_keys(info["Ad3"])
    browser.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(info["City"])
    browser.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(info["ZIP"])
    browser.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys(info["Country"])
    browser.find_element_by_xpath('//*[@id="cnb"]').send_keys(info["Card Number"])
    browser.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(info["Card Month"])
    browser.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(info["Card Year"])
    browser.find_element_by_xpath('//*[@id="vval"]').send_keys(info["CVV"])

    browser.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    browser.find_element_by_xpath('//*[@id="pay"]/input').click()

    t1 = time.time()
    print(t1-t0)

    time.sleep(7200)

if __name__ == "__main__":
    main()
