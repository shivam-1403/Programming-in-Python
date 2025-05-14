from selenium import webdriver
import keyboard
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_driver_path = Service(r"D:\Developer\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.2f889ce0-246f-467a-a086-d9a721167240&dib=eyJ2IjoiMSJ9.2EzBddTDEktLY8ckTsraM27nKsa9jZ2u6fBw_GWjE7fb9025u5Vqfi2M5NvLs-H7h_ZZ7Yadd3yAp36cnguad7rltRGjFSnhiWPpJSbsczN56WAsDOF2e7unKCgf5y5cCf_JaBbJ5y50NaxvxbFu_Of2TgtlA0HPrpe1XNgAN5uYOav5-uweweFC4NvGDjtqgz0WBBbheWIysgE1k6QBhrK6zFIeVJkN70r2PLRnI80.Wh6OGeVhx5SQWvE5KRsJx0iyxgwd44uzHB3hany1zns&dib_tag=se&keywords=cooker&pd_rd_r=2672de9c-a5e2-40ec-8954-4932f15e8ddd&pd_rd_w=w1H9A&pd_rd_wg=2BGpe&qid=1744443208&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

time.sleep(10)
title = driver.find_element(By.NAME,'field-keywords')
print(title.get_attribute("placeholder"))

while True:
    if keyboard.is_pressed("esc"):
        driver.quit()
        break