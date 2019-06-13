from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PBot import getItem
import time

info = {
    "name"  : "Mark Micosa",
    "email" : "mark.18.micosa@gmail.com",
    "tel"   : "0838781053",
    "ad1"   : "136 Steeplechase Green",
    "ad2"   : "Skryne Road",
    "ad3"   : "Ratoath",
    "city"  : "Meath",
    "post"  : "A85 FH60",
    "loc"   : "UK (N.IRELAND)",
}

def main():
    t0 = time.time()
    browser = webdriver.Chrome('/home/philip/Downloads/chromedriver')
    item = 'https://www.supremenewyork.com' + getItem()
    browser.get(item)
    # browser.get('https://www.supremenewyork.com/shop/jackets/f56swlajm/wl72m9dws')

    browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(9)

    browser.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    browser.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(info["name"])
    browser.find_element_by_xpath('//*[@id="order_email"]').send_keys(info["email"])
    browser.find_element_by_xpath('//*[@id="order_tel"]').send_keys(info["tel"])
    browser.find_element_by_xpath('//*[@id="bo"]').send_keys(info["ad1"])
    browser.find_element_by_xpath('//*[@id="oba3"]').send_keys(info["ad2"])
    browser.find_element_by_xpath('//*[@id="order_billing_address_3"]').send_keys(info["ad3"])
    browser.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(info["city"])
    browser.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(info["post"])
    browser.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys(info["loc"])

    t1 = time.time()
    print(t1-t0)
    #chrome_options.add_experimental_option("detach", True)

if __name__ == "__main__":
    main()
