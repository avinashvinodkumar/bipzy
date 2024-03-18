import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions

def run():
    opt = Options()
    opt.add_experimental_option("debuggerAddress","localhost:8989")
    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extention",chrome_options=opt)
    #driver.maximize_window()
    driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")
    driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()
    driver.find_element("id","Token Address").send_keys("0x267d2E10f0A879B77275cfFd298DbFf81FCb499a")
    #time.sleep(20)
    #wait = WebDriverWait(driver, 6)
    #driver.implicitly_wait(10)
    #a=driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    #a=driver.find_element(By.XPATH, "// html[1] // body[1] // div[1] // div[2] // div[4] // div[1] // div[1] // div[2] // div[1] // button[1]")
    #print(a)
    #a.click()
    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    #driver.execute_script("arguments[0].scrollIntoView();", element)
    #driver.execute_script("window.scrollBy(0, 200);")
    wait = WebDriverWait(driver, 26)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))
    action = ActionChains(driver)
    action.move_to_element(element)
    #action.move_by_offset(x_offset, y_offset)
    action.click().perform()
    print(element)
    element.click()
    #driver.quit()
    time.sleep(10)

if __name__ == '__main__':
    run()