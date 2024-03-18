import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def run():
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extention\\chromedriver", options=options)
    driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")
    driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()
    #time.sleep(10)
    driver.find_element(By.ID, "Token Address").send_keys("0x88dd1F871dE13f7570fc19e1C20D9b66f6D6C00D")
    time.sleep(6)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(4)

    #driver.find_element(By.XPATH,"//button[contains(@class, 'media-library-dropzone-add')]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-1.jpg")
    #element = driver.find_element(By.XPATH,'//div[@class="media-library-help"]/span').send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-1.jpg")
    file_input = driver.find_element(By.XPATH, '//input[@class="media-library-hidden"]')
    file_input.send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-1.jpg")

    wait = WebDriverWait(driver, 20)
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(@class, 'media-library-dropzone-add')]")))
   ## driver.find_element_by_link_text('C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg').click()
    #frame_index = 0  # Replace with the actual index of the frame
   # driver.switch_to.frame(frame_index)

    #frame_name1 = 1 # Replace with the actual name or id of the frame
    #driver.switch_to.frame(frame_name1)

    #button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'media-library-dropzone-add')]")))
    #button.click()

    #file_input = driver.find_element(By.CSS_SELECTOR, "input.media-library-hidden")
    #file_input.send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")

    # Continue with further actions after the file upload

    #driver.find_element(By.XPATH,"//body/div[@id='__next']/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/div[2]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")

   # wait = WebDriverWait(driver, 20)
    #button = driver.find_element(By.CLASS_NAME, 'media-library-dropzone-add').send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")
    #button.click()

   # frame_reference = driver.find_element(By.ID, "//button[contains(@class, 'media-library-dropzone-add')]")
    #driver.switch_to.frame(frame_reference)

    #frame_reference = driver.find_element(By.XPATH, "//button[contains(@class, 'media-library-dropzone-add')]")
    #driver.switch_to.frame(frame_reference)

    #driver.switch_to.frame(frame_reference)
    #button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'media-library-dropzone-add')]")))

    # Locate the file input element
   # file_input = driver.find_element(By.XPATH, "//input[@type='file']")

    # Enter the file path into the file input
   # file_input.send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")

    # Click the button
    #button.click()
    #file_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "media-library-dropzone-add")]')))
    #file_button.click()

    #file_input = driver.find_element(By.XPATH, '//input[@class="media-library-hidden"]')
   # file_input.send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")

    #wait = WebDriverWait(driver, 10)  # Adjust the timeout duration if needed
    #wait = WebDriverWait(driver, 20)
    #element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.media-library-dropzone-add')))
   # element.send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")

    #file_input = driver.find_element(By.XPATH, '//input[@class="media-library-hidden"]')
    #file_input.send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")
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

    #driver.find_element(By.XPATH, "//label[contains(text(),'Start Time (UTC)*')]").click()
    #driver.find_element(By.XPATH, "//div[@class='react-datepicker__day'][contains(@aria-label,'June 20th 2023')]").click()

    driver.find_element(By.ID, "Liquidity Lockup (Days)*").send_keys("31")
    time.sleep(5)

    # date_time_values = ["02/06/2023 12:17 PM", "03/06/2023 11:50 PM"]



    # wait = WebDriverWait(driver, 10)
    # start_time_input = wait.until(EC.visibility_of_element_located((By.ID, "startTime")))
    # start_time_input.clear()
    # start_time_input.send_keys("02/06/2023 01:55 PM")

    # for value in date_time_values:
    # dtime_input = driver.find_element(By.ID, "timeInput")
    # time_input.clear()
    # time_input.send_keys(time)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(10)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    driver.execute_script(offset, element)
    time.sleep(5)

    #element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    #offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
    #driver.execute_script(offset, element)
   # time.sleep(5)

    #wait = WebDriverWait(driver, 10)
   # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))
   # element.click()

    #element = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    #offset = "arguments[0].dispatchEvent(new MouseEvent('click', {clientX: 5, clientY: 5, bubbles: true, cancelable: true}));"
   # driver.execute_script(offset, element)

    #driver.find_element(By.XPATH,"//button[contains(text(),'Submit')]").click()
    # driver.find_element(By.XPATH,"//button[contains(text(), 'Submit')]").click()
    #element = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    #driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #element.click()

    wait = WebDriverWait(driver, 10)
    element = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    driver.execute_script("arguments[0].click();", element)

    #element = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[7]/div/div/label/div[2]/button')
   # driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #element.click()
    #driver.switch_to_alert()
    #popup = driver.switch_to_Metamask()
    #time.sleep(4)
    #click_button = driver.find_element(By.XPATH, "//'Use default')]").click()
    #click_button.click()

    #click_button = driver.find_element(By.XPATH, '//button[@class="button btn--rounded btn-primary page-container__footer-button")]').click()
    #click_button.click()

    #driver.find_element(By.XPATH, "//'Confirm')]").click()

    #driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
    #parentwindowhandle = driver.window_handles()
   # print("the parent handle is" + parentwindowhandle)

   # driver.switch_to_window(handle)

    #driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()

    #parent_window_handle = driver.window_handles[0]
    #print("The parent handle is: " + parent_window_handle)

    #window_handles = driver.window_handles
    #driver.switch_to.window(window_handles[1])

    #driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
    driver.implicitly_wait(10)  # Wait for 10 seconds for elements to load
    element = driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]")
    element.click()

    time.sleep(10)
    driver.quit()

if __name__ == '__main__':
   run()