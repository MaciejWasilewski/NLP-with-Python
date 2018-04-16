#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:55:52 2018

@author: maciej
"""

import nltk
nltk.download()
from nltk.book import *
text1.concordance('monstrous')
text1.similar("monstrous")
text1.generate()
1/(len(set(text5))/len(text5))
text5.count('lol')/len(text5)
fdist=FreqDist(text1)
voc1=fdist.keys()
type(voc1)
fdist.plot(50, cumulative=False)
voc1[:50]
fdist.hapaxes()
sorted([word for word in set(text1) if len(word)>=7 and fdist[word]>7])
text1.collocations()
text5.collocations()
fdist=FreqDist([len(w) for w in text1])
fdist.keys()
fdist.items()
len(set([word.lower() for word in text1 if word.isalpha()]))
3*sent1
text2.dispersion_plot(["Elinor","Marianne","Edward","Willoughby"])
text5.collocations()
text2[-2:]
len(set(sent1+sent2+sent3+sent4+sent5+sent6+sent7))/len(sent1+sent2+sent3+sent4+sent5+sent6+sent7)
temp=FreqDist([w for w in text4 if len(w)==4])
list(temp.keys())[:10]
[word for word in text6 if "pt" in word]

"dize".endswith('ize')