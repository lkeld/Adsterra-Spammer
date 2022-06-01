import selenium
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

#Sets Chromedriver as headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# Loads Website
driver = webdriver.Chrome()
driver.get("https://lukedev.me/hosting/spamthis.html")

# Load Proxies
f = open("proxies.txt", "r")



