# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#      Web Scraping
# --------------------------

## News title, link scraping

from webscrap import wlog
from webscrap import wscrap

# Define log file location
wlog.set_custom_log_info('html/error.log')

'''
# Testing log file reporting
try:
    raise Exception
except Exception as e:
    wlog.report(str(e))
'''

news_scrap = wscrap.NewsScraper(wscrap.url_aj, wlog)

## UNCOMMENT THE FOLLOWING 2 LINES OF CODE TO GET SITE'S LATEST DATA
## OTHERWISE THIS PROGRAM PARSE DATA FROM DISK FILE RETRIEVED PREVIOUSLY

#news_scrap.retrieve_webpage()
#news_scrap.write_webpage_as_html()

news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
#news_scrap.print_beautiful_soup()
news_scrap.parse_soup_to_simple_html()
