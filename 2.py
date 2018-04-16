#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 18:22:01 2018

@author: maciej
"""

from nltk.corpus import gutenberg
from nltk import Text
gutenberg.fileids()
emma=gutenberg.words('austen-emma.txt')
emma=Text(emma)
emma.concordance("surprize")
for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.sents(fileid))
    num_vocab=len(set([w.lower()  for w in gutenberg.words(fileid)]))
    print((num_chars/num_words, num_words/num_sents,num_words/num_vocab, fileid))
    
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print((fileid, webtext.raw(fileid)[:65]))
    
from nltk.corpus import brown
from nltk import FreqDist
brown.categories()
news_text=brown.words(categories="news")
gov=brown.words(categories='government')
fdist=FreqDist([w.lower() for w in news_text])
fdist_gov=FreqDist([w.lower() for w in gov])
modals=["can","could", "may", "might","must", "will"]
for m in modals:
    print(m+': '+str(fdist_gov[m]/fdist_gov[modals[0]])+" "+str(fdist[m]/fdist_gov[modals[0]]))
from nltk import ConditionalFreqDist
cfd=ConditionalFreqDist((genre, word) for genre in brown.categories()
                        for word in [word.lower() for word in brown.words(categories=genre)])
days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
cfd.tabulate(conditions=['news', 'romance'], samples=days)
