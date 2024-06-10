import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config

city = config.CITY
filter_lang = config.LANG
url = config.URL
search_city_textbox = config.SEARCH_CITY_TEXTBOX
home_screen_city_display = config.HOME_SCREEN_DISPLAY_SELCTED_CITY
home_screen_search_bar = config.HOME_SCREEN_SEARCH_BAR
language_filter = config.LANGUAGE_FILTER

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options = options)
driver.get(url)
print(driver.title)
element = driver.find_element(By.XPATH,search_city_textbox)
element.send_keys(config.CITY)
time.sleep(2)
element.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
City = driver.find_element(By.XPATH,home_screen_city_display)
print(City.text)
assert city == City.text
try:
    driver.find_element(By.ID,home_screen_search_bar).click()
    time.sleep(5)
    driver.find_element(By.XPATH,language_filter).send_keys(filter_lang).click()

except BaseException:
    print("Execution not complted need to handle the error")

finally:
    driver.quit()


