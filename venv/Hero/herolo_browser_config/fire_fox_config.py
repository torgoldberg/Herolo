from selenium import webdriver

"""
This file present the fie fox browser configuration for the project
"""

driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get('???')
delay = 3