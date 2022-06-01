import selenium
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

#Sets Chromedriver Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f'--proxy-server={proxy})

# Loads Website
driver = webdriver.Chrome()
driver.get("https://lukedev.me/hosting/spamthis.html")

# Load Proxies
f = open("proxies.txt", "r")
list_of_lines = f.readlines()
if not any("x " in s for s in list_of_lines): # add locator to first item in file when running for first the time
    list_of_lines[0] = "x " + list_of_lines[0]
for index, line in enumerate(list_of_lines):
    if "x " in line:
        next_index = index + 1
        if index == len(list_of_lines) -1:
            next_index = 0

        list_of_lines[index] = list_of_lines[index].split("x ").pop() # update current line
        proxy = list_of_lines[index]
        list_of_lines[next_index] = "x " + list_of_lines[next_index] # update next line
        break


