# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#  Download Sequentially
# --------------------------

import os
import time 
import sys 

import requests 


SOURCE_URL = "http://flags.fmcdn.net/data/flags/w1160"
FILE_EXT   = ".png"
SAVE_DIR   = "images/"
COUNTRIES  = "bd br gb us in my th pk fr sn hk gr".split()

def save_image(image, name):
    path = os.path.join(SAVE_DIR, name)
    with open(path, 'wb') as fp:
        fp.write(image)
        
def download_image(country):
    url = f'{SOURCE_URL}/{country}{FILE_EXT}'
    try:
        resp = requests.get(url)
    except:
        return None 
    
    return resp.content
    
def debug_msg(msg):
    print(msg, end = ' ')
    sys.stdout.flush()
    
def saving_file_name(country):
    return f"{country}{FILE_EXT}"
    
def download_all(countries):
    for country in countries:
        image = download_image(country)
        debug_msg(country)
        save_image(image, saving_file_name(country))
    
    return len(countries)
    
def main(func):
    time_start = time.time()
    count = func(COUNTRIES)
    time_end = time.time()
    
    duration = time_end - time_start 
    print(f"\n{count} images downloaded in {duration:.2f} seconds")
    
# entry point 
if __name__ == '__main__':
    main(download_all)