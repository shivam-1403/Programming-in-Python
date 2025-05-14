from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard

chrome_driver_path = Service(r"D:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, 'fName')
fname.send_keys("Shivam")
lname = driver.find_element(By.NAME, 'lName')
lname.send_keys("Thakral")
mail = driver.find_element(By.NAME, 'email')
mail.send_keys("shivamthakral770@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR, 'form button')
submit.click()

while True:
    if keyboard.is_pressed("esc"):
        driver.quit()
        break