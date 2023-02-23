import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import chrome_driver_path

PROMISED_DOWN = 100
PROMISED_UP = 100


class InternetSpeedBot:
    def __init__(self, options, service):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        more_opt_btn = self.driver.find_element(By.ID, "onetrust-pc-btn-handler")
        more_opt_btn.click()
        time.sleep(2)
        confirm_btn = self.driver.find_element(By.CLASS_NAME, "save-preference-btn-handler")
        confirm_btn.click()
        time.sleep(3)
        start_test = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start_test.click()
        time.sleep(2)
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        while self.up.text == "--":
            self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed")

    def print_speed_info(self):
        if float(self.down.text) < PROMISED_DOWN:
            print(f"Your download speed is only {self.down.text}. It should be {PROMISED_DOWN}.")
        else:
            print(f"Great! Your download speed is {self.down.text}")

        if float(self.up.text) < PROMISED_UP:
            print(f"Your upload speed is only {self.up.text}. It should be {PROMISED_UP}.")
        else:
            print(f"Great! Your upload speed is {self.up.text}")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(chrome_driver_path)

internet_speed_bot = InternetSpeedBot(options, service)
internet_speed_bot.get_internet_speed()
internet_speed_bot.print_speed_info()
