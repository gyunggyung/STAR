from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.lyrics.co.kr/?p=225468")
bsObj = BeautifulSoup(html, "html.parser")
lyrics = str(bsObj.find("p"))
print(lyrics)
print("="*200)
lyrics.replace("<br>","\n")
lyrics.replace("</br>","\n")
lyrics.replace("사람","악마")
print(lyrics)

f = open("lyrics.txt",'w')
f.write(str(lyrics))
f.close()
