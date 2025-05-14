from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard

chrome_driver_path = Service(r"D:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get("http://en.wikipedia.org/wiki/Main_Page")

counts = driver.find_elements(By.CSS_SELECTOR, '#articlecount a')
# counts[1].click()
search = driver.find_element(By.NAME, 'search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)

while True:
    if keyboard.is_pressed("esc"):
        driver.quit()
        break