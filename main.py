from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_UP = 200
PROMISED_DOWN = 150
EMAIL = "udemyshitikanthapython@gmail.com"
PASSWORD = "Qwertyuiop@178"
USERNAME = "@an_airtel_user_"
chrome_driver_path = "C:/Development/chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.chrome_driver_path = driver_path
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(4)

        accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        sleep(1)
        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        sleep(40)

        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

        self.up = self.up.text
        self.down = self.down.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/signup")
        self.driver.maximize_window()
        sleep(5)

        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]').click()
        sleep(4)

        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(EMAIL)

        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        sleep(4)

        user_name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_name.send_keys(USERNAME)

        next_button_2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        sleep(4)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)
        sleep(4)

        log_in_2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        sleep(8)

        tweet = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        tweet.send_keys(f"Hey @airtelindia, why my internet speed is  {self.down}Mbps/{self.up}Mbps  when I pay for  {PROMISED_UP}Mbps/{PROMISED_DOWN}Mbps. ")

        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        post.click()
        sleep(8)


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
sleep(30)