from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import keyboard
import time

chrome_driver_path = Service(r"D:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")

event_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget li time')

event_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events = {}
for n in range(len(event_time)):
    events[n] = {
        "time" : event_time[n].text,
        "name" : event_name[n].text,
    }

print(events)

while True:
    if keyboard.is_pressed("esc"):
        driver.quit()
        break
