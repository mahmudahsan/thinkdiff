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
#      Web Crawler Bot
#      Mahmud Ahsan
# --------------------------
import scrapy

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/Books/b/ref=sv_b_4?ie=UTF8&node=549028']
    
    def parse(self, response):
        selector = response.css('a')
        
        dict_items = []
        for item in selector:
            title = item.css('.aok-block::attr(title)').extract_first()
            url = item.css('.aok-block::attr(href)').extract_first()
            img = item.css('img::attr(src)').extract_first()
            
            if title and url and img:
                di = (title, response.urljoin(url), img)
                dict_items += [di]
                
                yield {
                    'title':title,
                    'url':response.urljoin(url),
                    'img': img
                }

                # yield response.follow(response.urljoin(url), self.parse)
        self.write_as_html(dict_items)
        
    # write a html file
    def write_as_html(self, dict_items):
        htmltext = '''
 <html>
     <head><title>Amazon Book Crawler</title></head>
     <body>
         {LINKS}
     </body>
 </html>
 '''
        link_items = "<ol>"
        for x in dict_items:
            link_items += "<li> \
                             <span><img src='{}'></span> \
                             <span><a target='_blank' href='{}'>{}</a></span> \
                           </li>".format(x[2], x[1], x[0])
        link_items += "</ol>"
        htmltext = htmltext.format(LINKS=link_items)
        
        with open("azinfo.html", 'w') as fobj:
            fobj.write(htmltext)

    
