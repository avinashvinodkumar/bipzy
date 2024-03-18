from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("debuggerAddress", "localhost:8989")
#chrome_driver_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
#options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extension1\\chromedriver.exe", options=options)

driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")