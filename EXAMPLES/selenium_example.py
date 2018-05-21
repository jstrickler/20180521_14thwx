#!/usr/bin/env python3
# (c) 2015 John Strickler
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('localhost:5000')

name_entry = driver.find_element_by_id('name')
if name_entry:
    quest_entry = driver.find_element_by_id('quest')
    name_entry.send_keys("King Arthur")
    quest_entry.send_keys('The GRRRRail')

    submit_button = driver.find_element_by_id('submit')

    submit_button.click()

    driver.implicitly_wait(30000)

    print driver.page_source

driver.close()



