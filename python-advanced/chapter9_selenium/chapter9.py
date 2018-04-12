# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
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

    # download Chrome Webdriver  
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    chrome_driver = os.path.join(os.getcwd(), "chromedriver")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    driver.get("https://github.com")
    assert "GitHub".lower() in driver.title.lower()
    
    # scrap info
    h1_elem = driver.find_element_by_tag_name("h1")
    print(h1_elem.text)

    # fill and submit form
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("python")
    elem.send_keys(Keys.RETURN)

    # screenshot capture
    driver.get_screenshot_as_file("python-github.png")
    driver.close()

if __name__ == '__main__' : main()