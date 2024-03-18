import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def run():
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extention\\chromedriver", options=options)
    driver.get("https://www.makemytrip.com/")
    driver.find_element(By.XPATH, "//span[contains(text(),'Departure')]").click()
    #departure_element = driver.find_element(By.XPATH, "//span[@class='lbl_input' and text()='Departure']").click()

    #driver.find_element(By.XPATH, "//div[@class='DayPicker-Day DayPicker-Day--selected'][@aria-label='Sat Jun 24 2023']").click()




    #time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    run()