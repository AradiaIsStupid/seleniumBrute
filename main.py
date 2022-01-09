from selenium import webdriver 
import random 
import time

brave_path = ""

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(chrome_options=option)
browser.get("")


passwordfinder = open("uwu.txt").read().splitlines()

for i in range(10000): 
    password = random.choice(passwordfinder)
    browser.find_element_by_name('code').send_keys(password)
    submit = browser.find_element_by_name('check')
    submit.click()



