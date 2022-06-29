from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime

PATH = r"C:\Users\Yatharth\Downloads\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

driver.get(url)

_path = '/html/body/c-wiz[1]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/h3/a'

# link = driver.find_element_by_xpath(_path)

while(True):
    now = datetime.now()
      

    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} IST')
    c = 1
    for x in range(3, 9):
        curr_path=''

        try:
            curr_path = f'/html/body/c-wiz[1]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[{x}]/div/div/article/h3/a'
            title = driver.find_element(by= By.XPATH, value=curr_path)
        
        except:
            continue      
        
        print(f"Heading {c}: ")
        c += 1        
        print(title.text)    
    time.sleep(10)


