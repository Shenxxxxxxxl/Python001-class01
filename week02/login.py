import requests
from selenium import webdriver
chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
browser = webdriver.Chrome(executable_path= chromePath)
browser.get('https://shimo.im/welcome')
browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]').click()
browser.find_element_by_xpath('//input[@type="text"]').send_keys('*****')
browser.find_element_by_xpath('//input[@type="password"]').send_keys('****')
browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()
cookies = browser.get_cookies()
print(cookies)