from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.FirefoxOptions()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Path to your Firefox executable
options.add_argument("--marionette-port=8989")

driver = webdriver.Firefox(executable_path="C:\\Users\\HP\\Desktop\\Add extention\\geckodriver.exe", options=options)
driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")

driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()
driver.find_element(By.ID, "Token Address").send_keys("0x88dd1F871dE13f7570fc19e1C20D9b66f6D6C00D")
time.sleep(4)

# Rest of your code...
