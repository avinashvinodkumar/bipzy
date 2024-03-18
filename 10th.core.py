from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    #options = webdriver.ChromeOptions()
    #options.add_argument("--start-maximized")

    #options = Options()
    #options.add_experimental_option("debuggerAddress", "localhost:8989")
    #driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extention\\chromedriver", options=options)
    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extention\\chromedriver1.exe")

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

    #driver.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[2]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-1.jpg")
    #driver.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/div[2]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")
    #element = driver.find_element_by_xpath("//span[contains(text(), 'Select or drag max 1 file | PNG, JPEG, JPG')]")
    #element = driver.find_element_by_xpath("//span[text() = 'Select or drag max 1 file | PNG, JPEG, JPG']")
    element = driver.find_element_by_xpath("//div[@class='media-library-help']/span[text()='Select or drag max 1 file | PNG, JPEG, JPG']")
    element = driver.find_element_by_xpath("//div[@class='media-library-help']/span")
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
    #element = driver.find_element(By.XPATH,"//input[@id='startTime']").click()


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

    #wait = WebDriverWait(driver, 10)

    #driver = webdriver.Chrome("path/to/chromedriver")

    # Assuming driver is already on the page containing the button
   # button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    #button.click()

    wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
    print("test122..")
    #driver.execute_script("arguments[0].scrollIntoView();", button)

    # Click the button
    #button.click()
    #button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Submit']")))
    #button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))
   # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))   # Click the button
    #button.click()

   # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))

    # Scroll to the element
    #driver.execute_script("arguments[0].scrollIntoView();", button)

    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)

    # Wait for the button to be clickable
    button_xpath = "//button[contains(text(),'Submit')]"
    button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", button)

    # Click the button
    button.click()

    # Click the button
   # button.click()

    time.sleep(10)
    #driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
    #print("test11..")
    #button.click()
    print("test..")
    #window_handles = driver.window_handles
    #driver.switch_to.window(window_handles[-1])
    #button = driver.find_element_by_xpath("//button[@class='button btn--rounded btn-primary page-container__footer-button' and @data-testid='page-container-footer-next' and @role='button' and @tabindex='0' and @disabled='true']")
    #button.click()

    #driver = webdriver.Chrome("path/to/chromedriver")

    # Assuming driver is already on the page containing the button

    window_handles = driver.window_handles
    print(window_handles)
    print(driver)
    driver.switch_to.window(window_handles[-1])
    print(driver.window_handles)
    #button = driver.find_element(By.CLASS_NAME, "//button[contains(@class, 'page-container__footer-button__cancel') and text()='Reject']")
    button = driver.find_element(By.XPATH, "//button[contains(@class, 'page-container__footer-button__cancel') and text()='Reject']")
    print(button)
    # Click the button
    button.click()
   # button.click()

    #driver.execute_script('window.open("");')

    # Switch to the new window
    #driver.switch_to.window(driver.window_handles[-1])
    # Wait for the Metamask extension to load (assuming the extension's iframe has id 'iframe-container')
   # iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, '__NEXT_DATA__')))

    # Perform actions on the Metamask extension (example: click on the 'Connect' button)
    #connect_button = driver.find_element(By.XPATH, "//button[contains(text(),'Reject')]")
    #connect_button.click()

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    run()