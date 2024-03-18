#print(((ans)))
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_extension('metamask.crx')
#driver = webdriver.Chrome('./chrome.drive', options.chrome_options)
#chrome_options.debugger_address = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#driver = webdriver.Chrome(options=chrome_options)
#chrome_options = Options()
#chrome_options.add_extension(extension_path)
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#chrome_driver_path =("/Program Files (x86)\Google\Chrome\Application\chrome.exe\to\C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#driver = webdriver.Chrome(executable_path=chrome_driver_path)
#webdriver.Chrome()
#driver = webdriver.Chrome()
#driver.get('https://www.example.com')
#driver = webdriver.Chrome()
# print(type(webdriver.Chrome))
driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()
#driver.findElementsByXPath("//button[contains(text(),'Connect Wallet')]").click()
#driver.find_element(By.XPATH, '//button[tebutton[contains(text(),'Connect Wallet'xt()="flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm"]').click()
#driver.find_element(By.XPATH, "//button class[test()='flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm']").click()
#driver.find_element(By.Class_Name,"flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm").click
#a=driver.find_element_by_class_button("flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm")
#print(a)
#button = driver.find_element("class","flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm>Connect Wallet").click()
#button = driver.find_element_by_class_name#driver.find_element_by_x

#driver.find_element_by_class_button()
#driver.find_element_by_xpath("//button[@class='flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm>Connect Wallet']").click()
#driver.find_element("By.XPATH", "//button[@class='flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm>Connect Wallet']").click()
#driver.find_element("button class","flex justify-center items-center bg-primary-green w-max rounded-old-full py-2 px-2.5 text-sm").click()
# driver.find_element_by_id("Token Address").send_keys("0x2C643E35060D55C03Ba7e3534518E23f962666bd")
# driver.find_element_by_class_buttonid("Token Address").send_keys("0x2C643E35060D55C03Ba7e3534518E23f962666bd")
# driver.find_element_by_name("tokenAddress").send_keys("0x2C643E35060D55C03Ba7e3534518E23f962666bd")
driver.find_element("id","Token Address").send_keys("0x790fDe4912d5438Cd0fFEDC8aa42bbe77D95b4C1")
#driver.quit()
time.sleep(20)