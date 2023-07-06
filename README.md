# twitter-bot

The Internet Speed Checker is a Python script that uses Selenium and the Chrome WebDriver to perform a speed test on speedtest.net. It checks the download and upload speeds and sends a tweet to Spectrum if the speeds are below the promised values or if the internet is not working.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- Selenium
- Chrome WebDriver (compatible with your Chrome browser version)

## Installation

1. Clone the repository: **git clone <repository-url>**
2. 2. Install the required dependencies: **pip install selenium**
3. Download the Chrome WebDriver and place it in the project directory. Make sure it matches your Chrome browser version. You can download it from the official ChromeDriver website: [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/)
4. Update the Twitter credentials in the `config.py` file with your own Twitter username and password:

``python
USER_NAME = 'Your_Twitter_Username'
PASSWORD = 'Your_Twitter_Password'

## Usage

- In the main script (main.py), set the driver_path variable to the path of the Chrome WebDriver: **driver_path = r'path/to/chromedriver.exe'**
- Open a terminal or command prompt and navigate to the project directory.
- Run the script: **python main.py**
- The script will perform a speed test on speedtest.net and print the download and upload speeds to the console. If the speeds are below the promised values or if the internet is not working, it will send a tweet to Spectrum.

## Customization

- The initial setup of the bot sends a tweet to Spectrum Internet. However, you can customize the script to send a tweet to your ISP instead. To do this, modify the send_tweet() method in the Bot class of speed_checker.py and update the Twitter handle accordingly.
- You can also customize the tweet message to fit your specific needs. The tweet messages are defined in the check_internet_speed() method of the Bot class in speed_checker.py. Adjust the messages to convey your internet speed concerns appropriately.
- Additionally, you can modify other aspects of the script to suit your requirements, such as adjusting the sleep time for the speed test or changing the expected download and upload speeds. These settings can be found and modified in the check_internet_speed() method of the Bot class in speed_checker.py. 
