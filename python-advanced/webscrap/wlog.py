# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#      Reporting Logs in text file
# --------------------------

import logging

def set_custom_log_info(filename):
    logging.basicConfig(filename=filename, level=logging.INFO)
    
def report(e:Exception):
    logging.exception(str(e))

