from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PBot import getItem
import time

def details():
    info = {}
    l = ["Name", "Email", "Tel", "Ad1", "Ad2", "Ad3", "City", "ZIP", "Loc", "Card", "Month", "Year", "CVV"]
    i = 0
    while i < 13:
        print(l[i] + ": ")
        info[l[i]] = input()
        i += 1
    return info

def main():
    info = details()
    t0 = time.time()
    browser = webdriver.Chrome('/home/philip/Downloads/chromedriver')
    check = True
    while check:
        try:
            item = 'https://www.supremenewyork.com' + getItem()
            check = False
        except:
            continue
    browser.get(item)

    browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    val = True
    while val:
        try:
            browser.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
            val = False
        except:
            continue

    browser.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(info["Name"])
    browser.find_element_by_xpath('//*[@id="order_email"]').send_keys(info["Email"])
    browser.find_element_by_xpath('//*[@id="order_tel"]').send_keys(info["Tel"])
    browser.find_element_by_xpath('//*[@id="bo"]').send_keys(info["Ad1"])
    browser.find_element_by_xpath('//*[@id="oba3"]').send_keys(info["Ad2"])
    browser.find_element_by_xpath('//*[@id="order_billing_address_3"]').send_keys(info["Ad3"])
    browser.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(info["City"])
    browser.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(info["ZIP"])
    browser.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys(info["Loc"])
    browser.find_element_by_xpath('//*[@id="cnb"]').send_keys(info["Card"])
    browser.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(info["Month"])
    browser.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(info["Year"])
    browser.find_element_by_xpath('//*[@id="vval"]').send_keys(info["CVV"])
    browser.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    browser.find_element_by_xpath('//*[@id="pay"]/input').click()

    t1 = time.time()
    print(t1-t0)
    chrome_options.add_experimental_option("detach", True)



if __name__ == "__main__":
    main()
