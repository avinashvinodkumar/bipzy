from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run():
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:8989")
    #chrome_driver_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\Add extention\\chromedriver", options=options)

    driver.get("https://www.pariopad.com/launchpad/create?blockchain=80001")

    driver.find_element(By.XPATH, "//button[contains(text(),'Connect Wallet')]").click()

    driver.find_element(By.ID, "Token Address").send_keys("0x88dd1F871dE13f7570fc19e1C20D9b66f6D6C00D")
    time.sleep(4)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    driver.execute_script("arguments[0].click();", element)

    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/input[1]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-1.jpg")
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/input[1]").send_keys("C:\\Users\\HP\\Desktop\\profile\\avt-2.jpg")

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    driver.execute_script("arguments[0].click();", element)

    driver.find_element(By.ID, "Presale Rate").send_keys("10")
    driver.find_element(By.ID, "Softcap (MATIC)*").send_keys(".002")
    driver.find_element(By.ID, "Hardcap (MATIC)*").send_keys(".004")
    driver.find_element(By.ID, "Minimum Buy (MATIC)*").send_keys(".001")
    driver.find_element(By.ID, "Maximum Buy (MATIC)*").send_keys(".004")
    driver.find_element(By.ID, "Liquidity (%)*").send_keys("51")
    driver.find_element(By.ID, "Listing Rate*").send_keys("10")
    driver.find_element(By.ID, "Liquidity Lockup (Days)*").send_keys("31")

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    driver.execute_script("arguments[0].click();", element)

    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)

    button_xpath = "//button[contains(text(),'Submit')]"
    button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])
    button = driver.find_element(By.XPATH, "//button[contains(@class, 'page-container__footer-button__cancel') and text()='Reject']")
    button.click()

    driver.quit()


if __name__ == '__main__':
    run()
