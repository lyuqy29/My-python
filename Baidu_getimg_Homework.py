# coding: utf-8
import urllib2
import urllib
import re
import os
import socket 
from HTMLParser import HTMLParser

class parseLinks(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.authors=[]
        self.current_info={}
        # 增加了一个变量
        self.current_url = []
        self.pattern=re.compile(r'<a .+>(.*)</a>',re.S)
        self.in_div = False
        self.in_a = False
        
    def handle_starttag(self, tag, attrs):
        def __attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None
        #
        # if tag =='div':
        #     print(attrs)
            # self.in_div=True
        
        if tag =='div' and __attr(attrs, 'class') == 'threadlist_author pull_right':
            self.in_div=True
            
                          
        if tag == 'a' and self.in_div:
            self.in_a =True
            index = "http://tieba.baidu.com"+ __attr(attrs, 'href')
            self.current_url.append(index)  
#             print self.current_url
        
    def handle_endtag(self, tag):
        if tag == 'div':
            self.in_div=False
        if tag == 'a':
            self.in_a = False

    def handle_data(self, data):
        if self.in_a:
            if data:
                self.authors.append(data)
                self.current_info=dict(zip(self.authors,self.current_url))
                global user_list
                user_list= self.current_info
#                 print self.current_info
            
#             print data
#             m=self.pattern.match(data)
#             if m:
#                  self.current_info['name']=m.group(1)
#                  self.authors.append(self.current_info)
#                  self.current_info={}

    # 增加了注释处理函数
    def handle_comment(self,data):
        lParser = parseLinks()
        lParser.feed(data.decode('utf-8'))
        
def get_user_pic ():
    
    
    for name,url in user_list.items():
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}                                       
        try:
            req=urllib2.Request(url=url,headers=headers)
            c=urllib2.urlopen(req)
            cont=c.read() 
        except socket.error:
            pass 
        pattern=re.compile('<a href="javascript:;" style="" class="userinfo_head"><img src="(.*?)".*>', re.S)
        pic_url= re.findall(pattern, cont)
        try:
            print pic_url[0]
        except IndexError:
            pass    
        Path = 'C:\Python-files\Pic_files\\'
        if not os.path.exists(Path):
            os.makedirs(Path)
        target=Path +'%s.jpg'%(name)
        try:
            urllib.urlretrieve(pic_url[0], target)
        except IndexError :
            pass
         
if __name__ == '__main__':
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}                                       
    url='http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
    req=urllib2.Request(url=url,headers=headers)
    c=urllib2.urlopen(req)
    cont=c.read()
    # print cont
    lParser = parseLinks()
    lParser.feed(cont)
    
    get_user_pic()
    
#     print lParser.authors
#     for name,url in aa.items():
#         print (name)
#         print (url)
#     print lParser.authors
    
    
    # print (lParser.authors)
