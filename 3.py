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

rotokas_words=nltk.corpus.toolbox.words('rotokas.dic')
cvs=[cons_vow for word in rotokas_words for cons_vow in re.findall(r'[^aeiou][aeiou]',word.lower())]
cfd=nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

cv_word_pairs=[(cv,w) for w in rotokas_words for cv in re.findall(r'[^aeiou][aeiou]',w.lower())]
cv_index=nltk.Index(cv_word_pairs)
cv_index['po']


def naive_stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

print(naive_stem('processing'))

re.findall(r'\b.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')

re.findall(r'\b.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)\b', 'processing')

re.findall(r'\b(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)\b', 'processing')

re.findall(r'\b(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)\b', 'processes')

re.findall(r'\b(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)\b', 'processes')

def naive_stem_re(word):
    found=re.findall(r'\b(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)\b', word)
    if found:
        stem, suffix = found[0]
    else:
        stem=word
    return stem

raw="""DENNIS: Listen, strange women lying in ponds distributing swords
... is no basis for a system of government. Supreme executive power derives from
... a mandate from the masses, not from some farcical aquatic ceremony."""

tokens=nltk.word_tokenize(raw)
[naive_stem_re(t) for t in tokens]

from nltk.corpus import brown

text=nltk.Text(brown.words(categories=['hobbies', 'learned']))

text.findall(r'<\w*> <and> <other> <\w*s>')

text.findall(r'<as> <\w*> <as> <the>? <\w*>')


porter=nltk.PorterStemmer()
lancaster=nltk.LancasterStemmer()

print([porter.stem(w) for w in tokens])
print([lancaster.stem(w) for w in tokens])

raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
... though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
... well without--Maybe it's always pepper that makes people hot-tempered,'..."""

print(re.split(" ", raw))
print(re.split(r"[ \n\t]+", raw))
print(re.split(r"\s+", raw))
print(re.split(r"\W+", raw))

print(re.findall(r'\w+|\S\w*',raw))
print(re.findall(r'\w+',raw))

print(re.findall(r'\w+(?:[-\']\w+)*', raw))