import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

config = configparser.ConfigParser()
config.read("config.ini",encoding="utf-8")

driver = webdriver.Chrome()

driver.get("https://moodle.chu.edu.tw/chu/irs/")

driver.find_element(By.ID,"txtAccount").send_keys(config.get('Config', 'studentNumber'))

driver.find_element(By.ID,"txtPwd").send_keys(config.get('Config', 'password'))

driver.find_element(By.CSS_SELECTOR,'[style="width:178px; height:50px;"]').click()

driver.implicitly_wait(5)

course_id = driver.find_element(By.XPATH, f"//*[contains(text(),'{config.get('Config','classCode')}')]").get_attribute('data-course-id')

driver.execute_script(f"irs_currentRollcall({course_id})")

driver.implicitly_wait(5)

while True:
    if driver.find_elements(By.XPATH,"//*[contains(@text,'開放簽到中')]"):
        driver.execute_script(f"makeRollcall({course_id})")
        break
    
    #print("Not Found")
    time.sleep(config.getint('Config','sleep'))
    driver.execute_script("location.reload()")


driver.quit()
