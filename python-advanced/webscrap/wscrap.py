'''
MIT License

Copyright (c) 2018 Mahmud Ahsan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
# --------------------------
#      Web Scraping
#      Mahmud Ahsan
# --------------------------

'''
urllib
BeautifulSoup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Installing Beautiful Soup
pip install beautifulsoup4

'''

from urllib.request import urlopen 
from bs4 import BeautifulSoup

# Global variables
url_aj   = 'http://www.aljazeera.com'
filepath = 'html/aj.html'
    
class NewsScraper:
    __url   = ''
    __data  = ''
    __wlog  = None
    __soup  = None 
    
    def __init__(self, url, wlog):
        self.__url  = url 
        self.__wlog = wlog 
    
    def retrieve_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print (e)
            self.__wlog.report(str(e))
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print ("Retrieved successfully")
            
    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
            
    def read_webpage_from_html(self, filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__data = fobj.read()
        except Exception as e:
            print (e)
            self.__wlog.report(str(e))
            
    def change_url(self, url):
        self.__url = url
            
    def print_data(self):
        print (self.__data)
    
    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, "html.parser")
        
    def parse_soup_to_simple_html(self):
        news_list = self.__soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) # h1
        
        #print (news_list)
        
        htmltext = '''
<html>
    <head><title>Simple News Link Scrapper</title></head>
    <body>
        {NEWS_LINKS}
    </body>
</html>
'''
        
        news_links = '<ol>'
        
        for tag in news_list:
            if tag.parent.get('href'):
                # print (self.__url + tag.parent.get('href'), tag.string)
                link  = self.__url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)
                
        news_links += '</ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)
        
        # print(htmltext)
        self.write_webpage_as_html(filepath="html/simplenews.html", data=htmltext.encode())
    
    
    def print_beautiful_soup(self):
        # print (self.__soup.title.string)
        news_list = self.__soup.find_all(['h1', 'h2', 'h4']) # h1
        
        #print (news_list)
        for tag in news_list:
            if tag.parent.get('href'):
                print (self.__url + tag.parent.get('href'), tag.string)
    
