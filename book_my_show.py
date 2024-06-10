import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


city = "Mumbai"
filter_lang = "TELGU"
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options = options)
driver.get("https://in.bookmyshow.com/")
print(driver.title)
element = driver.find_element(By.XPATH,"//input[@placeholder = 'Search for your city']")
element.send_keys(city)
time.sleep(2)
element.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
City = driver.find_element(By.XPATH,"//span[@class ='bwc__sc-1nbn7v6-10 cntvL ellipsis' and text()]")
print(City.text)
assert city == City.text
driver.find_element(By.ID,'4').click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class ='bwc__sc-m1rlyj-3 bwc__sc-3t17w7-25 bzIewT']").send_keys(filter_lang).click()
driver.quit()


