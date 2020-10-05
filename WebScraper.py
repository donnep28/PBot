#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

def compare(color_lst, item_lst):
    i = 0
    while i < len(color_lst):
        j = 0
        while j < len(item_lst):
            if color_lst[i].split(">")[0] == item_lst[j].split(">")[0]:
                return(item_lst[j])
            j += 1
        i += 1

def getItem(category, item, color):
    check = True
    while check:
        browser = webdriver.Chrome('/home/mark/Downloads/chromedriver')

        # Insert your URL to extract
        html = urlopen("http://www.supremenewyork.com/shop/all/" + category)
        bsObj = BeautifulSoup(html.read(), 'html.parser')

        item_lst = []
        color_lst = []
        for l in bsObj.find_all('a'):
            link = str(l)
            if item in link:
                item_lst.append(link)
            if color in link:
                color_lst.append(link)

        if len(item_lst) == 0:
            browser.quit()

        final = compare(color_lst, item_lst)
        if final:
            check = False
            browser.quit()

    return final.split('"')[3]
