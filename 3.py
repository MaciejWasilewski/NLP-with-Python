#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:52:11 2018

@author: maciej
"""

import nltk, re, pprint

from urllib.request import urlopen
url="http://www.gutenberg.org/files/2554/2554-0.txt"
raw=urlopen(url).read().decode("utf-8-sig")
type(raw)
len(raw)


raw.find("PART I")
raw.rfind("End of Project Gutenberg’s")
raw=raw[raw.find("PART I"):raw.rfind("End of Project Gutenberg’s")]
raw[:10]

tokens=nltk.word_tokenize(raw)
tokens[:10]
text=nltk.Text(tokens)
text[1020:1060]
text.collocations()

url2="http://news.bbc.co.uk/2/hi/health/2284783.stm"
html=urlopen(url2).read().decode('utf-8')
type(html)
html[:60]

print(html)
# clean_html depreciated
#raw_html=nltk.clean_html(html)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
raw_html=soup.get_text()
raw_html.find("The last natural blondes will die out within 200 years, scientists believe.")
raw_html=raw_html[raw_html.find("The last natural blondes will die out within 200 years, scientists believe."):raw_html.rfind(''"The frequency of blondes may drop but they won't disappear."'')+len(''"The frequency of blondes may drop but they won't disappear."'')+1]
tokens=nltk.word_tokenize(raw_html)
text=nltk.Text(tokens)
text.concordance('gene')

import feedparser
llog=feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
llog['feed']['title']
len(llog.entries)
post=llog.entries[2]
post.title
content=post.content[0].value
content[:70]
s22=BeautifulSoup(content, 'html.parser')
s22.get_text()
nltk.word_tokenize(s22.get_text())


from nltk.corpus import gutenberg
raw=gutenberg.raw('melville-moby_dick.txt')
fdist=nltk.FreqDist([ch.lower() for ch in raw if ch.isalpha()])
fdist.keys()
fdist.plot()