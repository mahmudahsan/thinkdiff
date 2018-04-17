# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Web Crawler Bot
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

    
