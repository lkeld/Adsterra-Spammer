from selenium import webdriver

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
        
        chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy})
driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver/chromedriver")
driver.get("http://httpbin.org/ip")
body_text = driver.find_element_by_tag_name('body').text
                            
                            
