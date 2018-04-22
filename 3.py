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
raw_html=raw_html[raw_html.find("""The last natural blondes will die out within 200 years,
                                scientists believe."""):raw_html.rfind('''"The 
                                frequency of blondes may drop but they won't 
                                disappear."'')+len(''"The frequency of blondes 
                                may drop but they won't disappear."''')+1]
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
import re
pattern_to_tokenize=r'''(?x)    # set flag to allow verbose regexp
(?:[A-Z]\.)+                    # abbreviations
|[a-zA-Z]+(?:-[a-zA-Z]+)*       # words with optional internal hyphens
|[a-zA-Z]*\w*[a-zA-Z]+          # words with numbers inside them (but with no hyphyn)
|(?:\$?\d+(?:\.\d+)?%?)  # numbers around non-alpha
|\.\.\.                         # ellipsis
| [][.,;"'?():-_`]              # these are separate tokens
'''

import nltk
print(nltk.regexp_tokenize('That U.S.A. poster-print costs $12.40...13.10', pattern_to_tokenize))

sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')

text=nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
ssents=sent_tokenizer.tokenize(text)
import pprint
pprint.pprint(ssents[171:181])

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg2="0100100100100001001001000010100100010010000100010010000"
seg1="0000000000000001000000000010000000000000000100000000000"

def segment(text, segs):
    words=[]
    last=0
    for i in range(len(segs)):
        if segs[i]=='1':
            words.append(text[last:i+1])
            last=i+1
    words.append(text[last:])
    return words

segment(text, seg1)
segment(text, seg2)


def evaluate(text, segs):
    words=segment(text, segs)
    words_num=len(words)
    lex_size=len(" ".join(list(set(words))))
    return words_num+lex_size

evaluate(text, seg1)
evaluate(text, seg2)

silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']
" ".join(silly)


#1

"""Define a string s = 'colorless'. Write a Python statement that changes this to
“colourless” using only the slice and concatenation operations."""

s='colorless'
print(s[:4]+'u'+s[4:])

#2
"""We can use the slice notation to remove morphological endings on words. For
example, 'dogs'[:-1] removes the last character of dogs, leaving dog. Use slice
notation to remove the affixes from these words (we’ve inserted a hyphen to indicate
the affix boundary, but omit this from your strings): dish-es, run-ning, nation-ality,
un-do, pre-heat."""

print("dishes"[:4],"running"[:3],"nationality"[:6],"undo"[2:], "preheat"[3:])

#7
"""Write regular expressions to match the following classes of strings:
a. A single determiner (assume that a, an, and the are the only determiners)
b. An arithmetic expression using integers, addition, and multiplication, such as
2*3+8"""

reg_exp_a=r"(?:\ban?\b|the)"

text=nltk.corpus.brown.raw(categories='humor')
import re

set(re.findall(reg_exp_a, text))

reg_exp_b=r"\d+(?:[\*\+]\d+)+"

re.findall(reg_exp_b, "2+2+3*55+4343 adam23+4*6")


#18

"""Read in some text from a corpus, tokenize it, and print the list of all wh-word
types that occur. (wh-words in English are used in questions, relative clauses, and
exclamations: who, which, what, and so on.) Print them in order. Are any words
duplicated in this list, because of the presence of case distinctions or punctuation?"""

text=nltk.corpus.brown.words(categories='humor')
wh_words=[w for w in text if re.search('^(?:(?:wh)|(?:Wh))[a-zA-Z]*$', w)]
import pprint
pprint.pprint(set(wh_words))

#19
"""Create a file consisting of words and (made up) frequencies, where each line
consists of a word, the space character, and a positive integer, e.g., fuzzy 53. Read
the file into a Python list using open(filename).readlines(). Next, break each line
into its two fields using split(), and convert the number into an integer using
int(). The result should be a list of the form: [['fuzzy', 53], ...]."""

with open("3_19.txt") as file:
    lines=file.readlines()
    
lines_formatted=[]

for item in lines:
    items=item.split()
    lines_formatted.append([items[0], int(items[1])])
    

#20
"""Write code to access a favorite web page and extract some text from it. For
example, access a weather site and extract the forecast top temperature for your
town or city today."""



from urllib.request import urlopen

from bs4 import BeautifulSoup

def check_temp():
    url="https://pogoda.onet.pl/prognoza-pogody/warszawa-357732"
    raw=urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(raw, 'html.parser')
    raw_html=soup.get_text()
    print("Teraz w Warszawie jest {0:s}C.".format(re.findall(r"""\w+"""+u"\u00B0", raw_html[raw_html.find("Pogoda"):raw_html.find("Godzinowa")])[0]))
check_temp()

#21
"""Write a function unknown() that takes a URL as its argument, and returns a list
of unknown words that occur on that web page. In order to do this, extract all
substrings consisting of lowercase letters (using re.findall()) and remove any
items from this set that occur in the Words Corpus (nltk.corpus.words). Try to
categorize these words manually and discuss your findings."""

path=r"http://www.tmz.com/2018/04/22/prince-paisley-park-enterprises-poetry-lyrics-photos-trademark/"
def unknown(url):
    raw=urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(raw, 'html.parser')
    raw_html=soup.get_text()
    corp=nltk.corpus.words.words()
    words_in_site=list(set(re.findall(r"\b[a-zA-Z][a-z]*\b", raw_html)))
    unknown_words=[w for w in words_in_site if w.lower() not in corp]
    print(unknown_words)
    
unknown(path)

#23

"""Are you able to write a regular expression to tokenize text in such a way that the
word don’t is tokenized into do and n’t? Explain why this regular expression won’t
work: «n't|\w+»."""

reg_exp=r"([a-zA-Z]+)(n't)*"
re.findall(reg_exp, "don't")

#24

"""Try to write code to convert text into hAck3r, using regular expressions and
substitution, where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. Normalize
the text to lowercase before converting it. Add more substitutions of your own.
Now try to map s to two different values: $ for word-initial s, and 5 for wordinternal s."""

text=r"""Try to write code to convert text into hAck3r, using regular expressions and
substitution, where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. Normalize
the text to lowercase before converting it. Add more substitutions of your own.
Now try to map s to two different values: $ for word-initial s, and 5 for wordinternal s."""
text=text.lower()
text=re.sub(r"e", "3", text)
text=re.sub(r"i", "1", text)
text=re.sub(r"o", "0", text)
text=re.sub(r"1", r"|", text)
text=re.sub(r"\w+(s)", r"5", text)
text=re.sub(r"\bs", r"$", text)
text=re.sub(r"\.", r"5w33t!", text)
text=re.sub(r"\bate\b", "8", text)
print(text)

#25

"""Pig Latin is a simple transformation of English text. Each word of the text is
converted as follows: move any consonant (or consonant cluster) that appears at
the start of the word to the end, then append ay, e.g., string → ingstray, idle →
idleay (see http://en.wikipedia.org/wiki/Pig_Latin).
a. Write a function to convert a word to Pig Latin.
b. Write code that converts text, instead of individual words.
c. Extend it further to preserve capitalization, to keep qu together (so that
quiet becomes ietquay, for example), and to detect when y is used as a consonant
(e.g., yellow) versus a vowel (e.g., style)."""

