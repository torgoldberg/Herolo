from selenium import webdriver

"""
This file present the chrome browser configuration for the project
"""

driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get('http://google.com')
delay = 3