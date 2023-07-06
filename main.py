from speed_checker import Bot
from config import USER_NAME, PASSWORD

driver_path = r'chromedriver.exe'

bot = Bot(driver_path=driver_path, twitter_user=USER_NAME, twitter_pass=PASSWORD)
bot.check_internet_speed()