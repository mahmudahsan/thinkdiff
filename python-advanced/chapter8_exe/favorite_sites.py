# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Executable in Windows 
# --------------------------

import webbrowser

def main():
    print("Openning Favorite Sites")
    
    with open("sites.txt") as fobj:
        try:
            for num, url in enumerate(fobj):
                webbrowser.open_new_tab(url.strip())
        except Exception as e:
            print(e)
        
    print("\nEnjoy!")
    
if __name__ == '__main__' : main()