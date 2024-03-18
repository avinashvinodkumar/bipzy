import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
chrome_options = ChromeOptions()

chrome_options.add_extension("C:\\Users\\HP\\PycharmProjects\\selenium demo\\matamask.crx")
driver = webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32.exe")
driver = webdriver.Chrome('./chrome.drive', options=chrome_options)
driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()
driver.find_element("id","Token Address").send_keys("0x790fDe4912d5438Cd0fFEDC8aa42bbe77D95b4C1")
#input('Press[ENTER] to close browser...')
#driver.quit()
time.sleep(20)