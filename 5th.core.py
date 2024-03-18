import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()
driver.find_element("id","Token Address").send_keys("0x790fDe4912d5438Cd0fFEDC8aa42bbe77D95b4C1")
#driver.quit()
time.sleep(30)


driver.find_element(By.XPATH, "//label[contains(text(),'Start Time (UTC)*')]").click()
    #driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--020 react-datepicker__day--selected react-datepicker__day--today']").click()
    #date_element = driver.find_element(By.XPATH,"//div[@class='react-datepicker__day react-datepicker__day--020 react-datepicker__day--selected react-datepicker__day--today']")
    #date_element.click()

//div[@class="react-datepicker__date"][contains(@aria-label,' June 21st, 2023')]
//div[@class="react-datepicker__day--023"][contains(@aria-label,' June 21st, 2023')]
react-datepicker__day--023
//div[@class="react-datepicker__date"][contains(text(),'04:00 PM')]

//div[@class='DayPicker-Day'][contains(@aria-label,' June 04 2023')]
//*[@id="startTime"]


//div[@class='react-datepicker__day react-datepicker__day--022 react-datepicker__day--today'][contains(@aria-label, 'June 22nd, 2023')]
//div[@class='react-datepicker__day react-datepicker__day--022 react-datepicker__day--today' and @aria-label='Choose Thursday, June 22nd, 2023']

#element = driver.find_element(By.XPATH, "//div[ @class ='react-datepicker__day react-datepicker__day--022 react-datepicker__day--today'][contains( @ aria-label, 'June 22nd, 2023')]").click()
     #button = driver.find_element(By.XPATH, "//button[contains(text(),'Open Popup')]")
     #button.click()
     #alert = driver.switch_to.alert
     #print("Popup Message:", popup_text)
     #alert.accept()
     #driver.switch_to.default_content()
     #element = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[7]/div/div/label/div[2]/button')
     #element.click()