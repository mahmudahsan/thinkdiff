#!/usr/bin/python
# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/mahmudahsanthinkdiff
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Executable in Windows 
# --------------------------

import webbrowser
import sys
import time

def main():
    print("Openning Favorite Sites")
    
    sites = "websites.txt" # default 
    browser = "safari" # default 
    
    if len(sys.argv) >= 2:
        sites = sys.argv[1].lower()
    if len(sys.argv) >= 3:
        browser = sys.argv[2].lower()
    
    for aa in sys.argv:
        print (aa)
    
    wbrowser = webbrowser.get(browser)
    
    with open(sites) as fobj:
        try:
            for num, url in enumerate(fobj):
                wbrowser.open_new_tab(url.strip())
                time.sleep(1)
        except Exception as e:
            print(e)
        
    print("\nEnjoy!")
    
if __name__ == '__main__' : main()