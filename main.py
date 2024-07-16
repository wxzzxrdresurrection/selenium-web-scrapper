from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Inicializa el WebDriver
driver = webdriver.Chrome()

driver.get("https://mx.aliexpress.com")
driver.maximize_window()

ad = driver.find_element(By.CLASS_NAME, "pop-close-btn").click()

input = driver.find_element(By.ID, "search-words").send_keys("Relojes")
button = driver.find_element(By.CLASS_NAME, "search--submit--2VTbd-T").click()

footer = driver.find_element(By.CLASS_NAME, "cards2023--pagination--1-0Grbh")
delta_y = footer.rect["y"]
delta_y = int(delta_y)
sleep(1)
ActionChains(driver)\
        .scroll_by_amount(0, delta_y)\
        .perform()

sleep(2)

titles = driver.find_elements(By.CLASS_NAME, "multi--titleText--nXeOvyr")

for title in titles:
    print(title.text)
    print("")