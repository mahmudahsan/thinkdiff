# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# youtube: https://www.youtube.com/c/mahmudahsanthinkdiff
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Execute JavaScript
# --------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024x1400")

    # download chrome driver https://sites.google.com/a/chromium.org/chromedriver/downloads and put exe file in same directory
    
    chrome_driver = os.path.join(os.getcwd(), "chromedriver")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    driver.get("https://github.com")
    assert "GitHub".lower() in driver.title.lower() # testing purpose

    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("python")
    elem.send_keys(Keys.RETURN)

    driver.get_screenshot_as_file("python-github.png")
    driver.close()

if __name__ == '__main__' : main()