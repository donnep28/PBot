#!/usr/bin/env python3

import time 
from bs4 import BeautifulSoup
from urllib.request import urlopen

def compare(color_lst, item_lst):
    i = 0
    while i < len(color_lst):
        j = 0
        while j < len(item_lst):
            if color_lst[i].split(">")[0] == item_lst[j].split(">")[0]:
                return(item_lst[j])
            j += 1
        i += 1

def main():
    t0 = time.time()

    html = urlopen("http://www.supremenewyork.com/shop/all/shoes") # Insert your URL to extract
    bsObj = BeautifulSoup(html.read(), 'html.parser')

    item = 'Jordan'
    color = 'White'
    
    item_lst = []
    color_lst = []
    for l in bsObj.find_all('a'):
        link = str(l)
        if item in link:
            item_lst.append(link)
        if color in link:
            color_lst.append(link)
    
    print(compare(color_lst, item_lst))
    t1 = time.time()
    print(t1-t0)

if __name__ == "__main__":
    main()