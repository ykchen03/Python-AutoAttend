import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')

driver = webdriver.Chrome()

driver.get('https://elearn.chu.edu.tw/?moodlelogin')

driver.find_element(By.ID,"txtAccount").send_keys(config.get('Config', 'studentNumber'))

driver.find_element(By.ID,"txtPwd").send_keys(config.get('Config', 'password'))

driver.find_element(By.CSS_SELECTOR,'[style="width:178px; height:50px;"]').click()

driver.implicitly_wait(5)

driver.get(driver.find_element(By.XPATH, f"//*[contains(@title,'{config.get('Config','classCode')}')]").get_attribute('href'))

driver.implicitly_wait(5)

driver.get(driver.find_element(By.XPATH, "//*[contains(@href,'attendance')]").get_attribute('href'))
#https://moodle.chu.edu.tw/mod/attendance/attendance.php?sessid=1503919&amp;sesskey=yaDkjaHTV3
driver.implicitly_wait(5)

while True:
    
    if driver.find_elements(By.XPATH,"//*[contains(@href,'ssessid')]"):
        driver.get(driver.find_element(By.XPATH, "//*[contains(@href,'ssessid')]").get_attribute('href'))
        break
    
    print('Not Found')
    time.sleep(config.getint('Config','sleep'))
    driver.refresh()


driver.quit()