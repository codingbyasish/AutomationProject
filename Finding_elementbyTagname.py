import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

   
    mp_btn = driver.find_elements(By.TAG_NAME, "a")
    mp_btn[5].click()



    time.sleep(5)
    # driver.close()
    driver.quit()
