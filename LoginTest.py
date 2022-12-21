


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://lichess.org/")
sleep(2)
loginBtn = driver.find_element(By.XPATH,"/html/body/header/div[2]/a")
loginBtnText = loginBtn.text
loginBtn.click()
sleep(5)


input= driver.find_element(By.NAME,"username")
input.send_keys("chessingtitanic")
sleep(2)
input= driver.find_element(By.NAME,"password")
input.send_keys("Ati171824")
sleep(3)
driver.maximize_window()
loginBtn = driver.find_element(By.XPATH,"/html/body/div/main/form/div[1]/button")
loginBtnText = loginBtn.text
loginBtn.click()
sleep(5)
donate = driver.find_element(By.XPATH,"/html/body/header/div[1]/a")
if donate.text == "BAĞIŞ YAP" :
 print("Başarılı")
else :
 print("Başarısız")









# if loginBtnText == "SIGN IN":
#    print("Test başarılı ")
# else:
#     print("Test Başarısız ")
# input()