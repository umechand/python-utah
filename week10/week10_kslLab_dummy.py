from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()

s = Service(ChromeDriverManager().install())
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service = s, options = chrome_options)


#Settings
classifieds_link = 'https://classifieds.ksl.com/search/furniture'
time_to_wait_between_checking = 15

def get_first_listing_info():
    driver.get(classifieds_link)
    time.sleep(5)
    link = driver.find_element(By.CSS_SELECTOR, "#search-results > div > section > div > div:nth-child(1) > section:nth-child(4) > div.listing-item-info > h2 > div > a").get_attribute('href')
    title = driver.find_element(By.CSS_SELECTOR, "#search-results > div > section > div > div:nth-child(1) > section:nth-child(4) > div.listing-item-info > h2 > div > a").text
    return(link, title)

listing_info = get_first_listing_info()
first_listing_link_temp = listing_info[0]
title = listing_info[1]
print("First listing title: "+ title+ " Link: "+ first_listing_link_temp)

check_count = 0
while True:
    check_count += 1
    time.sleep(time_to_wait_between_checking)
    print('Checking to see if there is a new ad, this is attempt number '+ str(check_count))
    listing_info = get_first_listing_info()
    first_listing_link = listing_info[0]
    title = listing_info[1]
    if(first_listing_link_temp != first_listing_link):
        print("There is a new ad! title: "+title  + "Link : "+ first_listing_link)
        break
