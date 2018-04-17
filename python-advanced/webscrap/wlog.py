# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Reporting Logs in text file
# --------------------------

import logging

def set_custom_log_info(filename):
    logging.basicConfig(filename=filename, level=logging.INFO)
    
def report(e:Exception):
    logging.exception(str(e))

