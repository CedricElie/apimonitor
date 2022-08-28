import urllib
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
contents = html.read()
print(contents)