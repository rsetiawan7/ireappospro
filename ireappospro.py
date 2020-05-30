ireappospro

#import modul yang dibutuhkan
from selenium import webdriver
from bs4 import BeautifulSoup
from pdb import set_trace as bp ##for testing
import re
import time
import csv


#running chromedriver
outputFileName='result'
link = "https://play.google.com/store/apps/details?id=com.sterling.ireappro&showAllReviews=true"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(link)


#print title
title = driver.find_element_by_xpath('/html/head/meta[9]').get_attribute('content')

print(title)


# scrolling data
flag=0
while 1:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    try:
        loadMore=driver.find_element_by_xpath("//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ')]").click()
    except:
        time.sleep(1)
        flag=flag+1
        if flag >= 10:
            break
    else:
        flag=0
reviews=driver.find_elements_by_xpath("//*[@jsname='fk8dgd']//div[@class='d15Mdf bAhLNe']")


# 
reviews[0].text


# get reviews
reviews=driver.find_elements_by_xpath("//*[@jsname='fk8dgd']//div[@class='d15Mdf bAhLNe']")
i = 1
for review in reviews:
    print(str(review.text))


# menghitung jumlah data yang masuk dari chromedriver
print('data reviews terunduh '+str(len(reviews))+' buah')


# 


