#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Config
Webdriver download website https://www.seleniumhq.org/download/ 
Please get version same as your browser.
'''

from selenium import webdriver
WEBDRIVE_PATH = '/Users/xxx/Downloads/chrome'

INGRESS_GOOGLE_LOGIN_URL = 'https://accounts.google.com/signin/v2/identifier?service=ah&passive=true&continue=https%3A%2F%2Fappengine.google.com%2F_ah%2Fconflogin%3Fcontinue%3Dhttps%3A%2F%2Fintel.ingress.com%2Fintel&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

GOOGLE_EMAIL = ''
GOOGLE_PASSWORD = ''


if __name__ == "__main__":
    try:
        
        __dr = webdriver.Chrome(executable_path = WEBDRIVER_PATH)
        __dr.get(INGRESS_GOOGLE_LOGIN_URL)
        __dr.find_element_by_id('identifierId').send_keys(GOOGLE_EMAIL)
        __dr.find_element_by_xpath("//content/span").click()
        __dr.find_element_by_xpath('//input[@type="password"]').send_keys(GOOGLE_PASSWORD)
        __dr.find_element_by_id('passwordNext').click()
        
        my_cookies = dr.get_cookies()

    except :
        print('Something wrong...')

    



else:
    exit()