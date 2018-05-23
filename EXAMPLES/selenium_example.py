#!/usr/bin/env python3
# (c) 2015 John Strickler
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()

driver.get('http://127.0.0.1:5000/')

for link in driver.find_elements_by_tag_name('a'):
    print(link.get_attribute('innerHTML'))
    print('-' * 60)
    if 'Arthur' in link.get_attribute('innerHTML'):
        result = link.click()
        print(result)
#     quest_entry = driver.find_element_by_id('quest')
#     name_entry.send_keys("King Arthur")
#     quest_entry.send_keys('The GRRRRail')
# 
#     submit_button = driver.find_element_by_id('submit')
# 
#     submit_button.click()
# 
#     driver.implicitly_wait(30000)
# 
#     print driver.page_source

driver.close()



