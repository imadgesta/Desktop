from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# -------------------------------
browser = webdriver.Chrome()
# -------------------------------
browser.get("https://www.qa-practice.com/elements/button/simple")
# ---------------------------------------------------------------
click_button4 = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
click_button4.click()
# ---------------------------------------------------------------
sleep(5)