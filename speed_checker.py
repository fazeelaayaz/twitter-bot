import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bot:
    def __init__(self, driver_path, twitter_user, twitter_pass):
        self.driver_path = driver_path
        self.twitter_user = twitter_user
        self.twitter_pass = twitter_pass
        self.driver = None

    def check_internet_speed(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.speedtest.net/")

        promised_download = 500
        promised_upload = 200

        go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(45)  # Adjust sleep time based on the expected duration of the speed test

        down_result = self.driver.find_element(By.CSS_SELECTOR, '.result-item-download .result-data .result-data-large')
        up_result = self.driver.find_element(By.CSS_SELECTOR, '.result-item-upload .result-data .result-data-large')

        down_speed = float(down_result.text)
        up_speed = float(up_result.text)

        print("Download speed:", down_speed)
        print("Upload speed:", up_speed)

        if promised_download > down_speed or promised_upload > up_speed:
            self.send_tweet(
                f"Hey @Spectrum. My internet is below {promised_download} Mbps download and {promised_upload} Mbps upload."
            )

        elif down_speed == 0 and up_speed == 0:
            self.send_tweet("Hey @Spectrum. My internet is not working.")

        self.driver.quit()

    def send_tweet(self, message):
        if self.driver is None:
            service = Service(self.driver_path)
            self.driver = webdriver.Chrome(service=service)

        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)

        user = self.driver.find_element(By.NAME, 'username')
        user.send_keys(self.twitter_user)
        user.send_keys(Keys.ENTER)

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(self.twitter_pass)
        password.send_keys(Keys.ENTER)

        prompt = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        prompt.send_keys(message)
        prompt.send_keys(Keys.ENTER)

        self.driver.quit()
