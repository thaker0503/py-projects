from concurrent.futures import thread
from lib2to3.pgen2 import driver
from operator import imod
from selenium import webdriver
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By






def startBot(username,password,url):
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    

    
    driver.get(url)

    

    driver.find_element(by=By.CSS_SELECTOR, value="#name").send_keys(username)

    driver.find_element(by=By.CSS_SELECTOR, value="#email").send_keys(password)

    driver.find_element(by=By.CSS_SELECTOR, value="#signup > div:nth-child(4) > button").click()

username = "hellboy"
password = "harshbantuya@gmail.com"   

url = 'https://www.javascripttutorial.net/sample/dom/form/signup.html'

startBot(username,password,url)

