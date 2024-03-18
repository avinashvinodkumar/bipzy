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
from selenium.webdriver.chrome.service import Service


def run():
    options = webdriver.ChromeOptions()
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:8989")

    # Set the path to your newly downloaded ChromeDriver executable
    chrome_driver_path = "C:\\path\\to\\chromedriver.exe"

    options = webdriver.ChromeOptions()
    # Add any additional options you need
    # ...

    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    #chrome_driver_path = "C:\\path\\to\\new\\chromedriver"

    # Set Chrome options if needed
    #options = webdriver.ChromeOptions()
    # Add any options here

    # Create the WebDriver instance using the new ChromeDriver executable
    #driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extention\\chromedriver", options=options)
     #driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chrome - win64\\chrome - win64", options=options)

    driver.get("https://pariopad.com/launchpad/create?blockchain=80001")
    driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()
    #time.sleep(10)
    driver.find_element(By.ID, "Token Address").send_keys("0x88dd1F871dE13f7570fc19e1C20D9b66f6D6C00D")
    time.sleep(4)
    # wait = WebDriverWait(driver, 26)
    # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)


    driver.find_element(By.XPATH,"//body/div[@id='__next']/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[2]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-1.jpg")
    driver.find_element(By.XPATH,"//body/div[@id='__next']/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/div[2]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")
    #element = driver.find_element_by_xpath("//span[text()='Select or drag max 1 file | PNG, JPEG, JPG']")
    element = driver.find_element_by_xpath("//span[contains(text(), 'Select or drag max 1 file | PNG, JPEG, JPG')]")

    time.sleep(4)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(4)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(4)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(4)

    driver.find_element(By.ID, "Presale Rate").send_keys("10")
    driver.find_element(By.ID, "Softcap (MATIC)*").send_keys(".002")
    driver.find_element(By.ID, "Hardcap (MATIC)*").send_keys(".004")
    driver.find_element(By.ID, "Minimum Buy (MATIC)*").send_keys(".001")
    driver.find_element(By.ID, "Maximum Buy (MATIC)*").send_keys(".004")
    driver.find_element(By.ID, "Liquidity (%)*").send_keys("51")
    driver.find_element(By.ID, "Listing Rate*").send_keys("10")
    driver.find_element(By.ID, "Liquidity Lockup (Days)*").send_keys("31")

   # date_time_values = ["02/06/2023 12:17 PM", "03/06/2023 11:50 PM"]

    #wait = WebDriverWait(driver, 10)
    #start_time_input = wait.until(EC.visibility_of_element_located((By.ID, "startTime")))
    #start_time_input.clear()
    #start_time_input.send_keys("02/06/2023 01:55 PM")

   # for value in date_time_values:
        #dtime_input = driver.find_element(By.ID, "timeInput")
        #time_input.clear()
       # time_input.send_keys(time)

    # else:



    #driver.find_element(By.XPATH,"//[@class ="react-datepicker__date"][contains( @ aria-label, ' June 21st, 2023')]").click()
    #driver.find_element(By.XPATH, "// div[@ class ="react-datepicker__date"][contains(text(), '04:00 PM')]").click()

    #start_time_input = driver.find_element(By.ID, "startTime")
   # start_time_input.clear()
    #start_time_input.send_keys("21/06/2023 04:00 PM")
    #driver.find_element(By.XPATH,"//body/div[@id='__next']/div[2]/div[4]/div[1]/div[1]/div[2]/form[1]/div[3]/div[11]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[4]/div[3]").click()
    #driver.find_element(By.XPATH, "//li[contains(text(),'04:00 PM')]").click()
    #wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//input[@id='startTime']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--028 react-datepicker__day--selected' and @aria-label='Choose Wednesday, June 28th, 2023']")

    #start_time_input.clear()
    #driver.find_element(By.XPATH,"//div[@class ="react-datepicker__day--023"][contains( @ aria-label, ' June 23rd, 2023')]").click()
    #driver.find_element(By.ID, "startTime").click()

    #end_time_input = driver.find_element(By.ID, "endTime")

    #end_time_input.clear()

    #driver.find_element(By.ID, "endTime").click()

    #driver.find_element(By.XPATH,"//div[contains(text(),'23')]").click()

   # class ="react-datepicker__date"][contains( @ aria-label, ' June 21st, 2023')]
    #end_time_input = driver.find_element(By.ID, "endTime")
    #end_time_input.clear()
    #driver.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[4]/div[1]/div[1]/div[2]/form[1]/div[3]/div[12]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[4]/div[4]").click()
    #driver.find_element(By.XPATH, "// li[contains(text(), '07:30 PM')]").click()
    #end_time_input = wait.until(EC.visibility_of_element_located((By.ID, "endTime")))

    #end_time_input.send_keys("21/06/2023 07:30 PM")

    #start_time = datetime.strptime(start_time_input.get_attribute("value"), "%m/%d/%Y %I:%M %p")
    #end_time = datetime.strptime(end_time_input.get_attribute("value"), "%m/%d/%Y %I:%M %p")

    #if end_time <= start_time:
        #print("End time should be greater than start time")

    #else:


    # driver.find_element(By.ID, "startTime").clear()
    #wait = WebDriverWait(driver, 10)
    #start_time_input = wait.until(EC.visibility_of_element_located((By.ID, "startTime")))

    # start_time_input = driver.find_element(By.ID, "startTime")
    # start_time_input.clear()
    # time.sleep(5)
    # start_time_input.send_keys("01/06/2023 02:55 PM")

    #start_time_input = driver.find_element(By.ID, "startTime")

    #start_time_input.clear()
    #time.sleep(5)
    # start_time_input.send_keys("01/06/2023 3:42 PM")

    #driver.execute_script("document.getElementById('startTime').value = '01/06/2023 02:50 PM'")

    # start_time_input.send_keys(Keys.SPACE)
    # start_time_input.send_keys("03:42 PM")

    #driver.find_element(By.ID, "startTime").click()
    # driver.execute_script("document.getElementById('startTime').value = '01/06/2023 02:30 PM'")
    # start_time_input.send_keys("2023", Keys.TAB, "06", Keys.TAB, "01", "03:30 PM")
    #time.sleep(5)

    #wait = WebDriverWait(driver, 10)
    #start_time_input = wait.until(EC.visibility_of_element_located((By.ID, "startTime")))
    #start_time_input.clear()

    #driver.execute_script("document.getElementById('startTime').value = '02/06/2023 11:50 AM'")


    #wait = WebDriverWait(driver, 10)
    #end_time_input = wait.until(EC.visibility_of_element_located((By.ID, "endTime")))
    #end_time_input.clear()

    #driver.execute_script("document.getElementById('endTime').value = '03/06/2023 10:50 AM'")
    #time.sleep(5)

    #start_time_input = driver.find_element(By.ID, "startTime")
    #start_time_input.send_keys("02/06/2023 11:55 AM")

    #wait = WebDriverWait(driver, 10)
    #end_time_input = wait.until(EC.visibility_of_element_located((By.ID, "endTime")))

    #end_time_input.clear()

    #driver.execute_script("document.getElementById('endTime').value = '03/06/2023 12:00 AM'")

    # driver.find_element(By.ID, "startTime").send_keys("10")
    # driver.find_element(By.ID, "Liquidity Lockup (Days)*").send_keys("31")

    # driver.find_element(By.ID, "startTime").clear()
    # time.sleep(10)
    # driver.find_element(By.ID, "startTime").send_keys("01/06/2023 11:25 AM").click()

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(10)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(5)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(5)


    element = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)


    driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    #driver.find_element(By.XPATH, "//button[contains(text(),'Use default')]").click()

   # driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[7]/div/div/label/div[2]/button').click()
   # offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
   #driver.execute_script(offset, element)
   # popup = driver.switch_to_Max()
    #popup.click()

    element = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[7]/div/div/label/div[2]/button')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

    #button = driver.find_element(By.XPATH, "//button[contains(text(),'Open Popup')]")
    #button.click()
    #alert = driver.switch_to.alert
    #print("Popup Message:", popup_text)
   # alert.accept()
    #driver.switch_to.default_content()
    #element = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[7]/div/div/label/div[2]/button')
    #element.click()
    #window_handles = driver.window_handles
    #driver.switch_to.window(window_handles[-1])
    # element.click()

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    run()

