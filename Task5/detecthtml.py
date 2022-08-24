import re 
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print(tag)
        if attributes:
            for name,value in attributes:
                print(f"-> {name} > {value}")
        
        
        
parser = MyHTMLParser()
html = ''.join([input().strip() for _ in range(int(input()))])
parser.feed(html)
