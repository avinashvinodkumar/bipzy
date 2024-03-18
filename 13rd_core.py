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
    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extension1", options=options)

    driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")
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

    driver.find_element(By.XPATH, "//input[@id='startTime']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--028 react-datepicker__day--selected' and @aria-label='Choose Wednesday, June 28th, 2023']")

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

