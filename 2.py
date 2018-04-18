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
cfd.
sent="In the beginning God created the heaven and the earth".split(sep=" ")+["."]
from nltk import bigrams
list(bigrams(sent))
#random text generator
import random
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        l1=list(cfdist[word].keys())
        l2=list(cfdist[word].values())
        temp=[]
        for i in range(len(l1)):
            temp=temp+[l1[i]]*l2[i]
        word=random.choice(temp)
    print(' ')
from nltk.corpus import genesis
text=genesis.words('english-kjv.txt')
bigram=bigrams(text)
cfd=ConditionalFreqDist(bigram)
generate_model(cfd, 'living', num=25)
import nltk
def unusual_words(text):
    text_vocab=set(w.lower() for w in text if w.isalpha())
    english_vocab=set(w.lower() for w in nltk.corpus.words.words())
    #unusual=[w for w in text_vocab if w not in english_vocab]
    unusual=text_vocab.difference(english_vocab)
    return sorted(unusual)

un=unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
from nltk.corpus import stopwords
stopwords.words('english')

def content_fraction(text):
    stopwords_temp=nltk.corpus.stopwords.words('english')
    l1=[w.lower() for w in text if w.isalpha()]
    l2=[w.lower() for w in text if w.isalpha() and w not in stopwords_temp]
    return len(l2)/len(l1)

print(content_fraction(nltk.corpus.reuters.words()))
import itertools

def how_many_words(letter_list, obligatory_letter, min_length=4):
    leng=min_length
    english_vocab=set(w.lower() for w in nltk.corpus.words.words())
    full=[]
    while leng!=0:
        temp_let=[list(i)+[obligatory_letter] for i in itertools.combinations(letter_list, leng-1)] 
        temp_words=list(set([w for w in ["".join(j) for i in temp_let for j in itertools.permutations(i)] if w in english_vocab]))
        full=full+temp_words
        leng=leng+1 if len(temp_words)!=0 else 0
    return full
wrds=how_many_words(['e','g','i','v','v','o','n','l'], 'r', min_length=3)

names=nltk.corpus.names
names.fileids()
[w for w in names.words('male.txt') if w in names.words('female.txt')]
cfd=nltk.ConditionalFreqDist([(fileid, name[-1]) for fileid in names.fileids() for name in names.words(fileid)])
cfd.plot()

entries=nltk.corpus.cmudict.entries()
len(entries)
for entry in entries[100:110]:
    print(entry)

for word, pron in entries:
    if len(pron)==3:
        p1,p2,p3=pron
        if p1=='P' and p3=='T':
            print(word, pron)

from nltk.corpus import swadesh
swadesh.fileids()
swadesh.words('en')
swadesh.entries(['pl', 'en'])
translate=dict(swadesh.entries(['pl', 'en']))
translate['dąć']

from nltk.corpus import toolbox
toolbox.entries('rotokas.dic')

from nltk.corpus import wordnet as wn
temp=wn.synsets('motorcar')
temp[0].definition()
for syn in wn.synsets('dish'):
    print(syn.hyponyms())
nltk.app.wordnet()
right=wn.synset('right_whale.n.01')
orca=wn.synset('orca.n.01')
minke=wn.synset('minke_whale.n.01')
tortoise=wn.synset('tortoise.n.01')
novel=wn.synset('novel.n.01')
right.lowest_common_hypernyms(minke)
right.lowest_common_hypernyms(orca)[0].min_depth()
right.path_similarity(minke)


#2
from nltk.corpus import gutenberg
gutenberg.fileids()
gutenberg.words('austen-emma.txt')
# word tokens
len([w.lower() for w in gutenberg.words('austen-emma.txt') if w.isalpha()])
#words
len(list(set([w.lower() for w in gutenberg.words('austen-emma.txt') if w.isalpha()])))

#3
from nltk.corpus import brown
brown.categories()
brown.words(categories='science_fiction')

#4
from nltk.corpus import state_union
state_union.fileids()
words=['men', 'women', 'people']
from nltk import ConditionalFreqDist
cfd=ConditionalFreqDist([(word, fileid) for fileid in state_union.fileids() for word in [w for w in state_union.words(fileid)]])
cfd.plot(conditions=words)

#5
word='life'
from nltk.corpus import wordnet as wn
for syn in wn.synsets(word): 
    for mer in syn.part_meronyms():
        print("Synset '{2}':\n\t{0}\n\npart meronym '{1}':\n\t{3} ".format(syn.definition(),
              mer.lemma_names()[0],syn.lemma_names()[0],mer.definition()))
        
    for mer in syn.member_meronyms():
        print("Synset '{2}':\n\t{0}\n\nmember meronym '{1}':\n\t{3} ".format(syn.definition(),
              mer.lemma_names()[0],syn.lemma_names()[0],mer.definition()))
    for mer in syn.substance_meronyms():
        print("Synset '{2}':\n\t{0}\n\nsubstance meronym '{1}':\n\t{3} ".format(syn.definition(),
              mer.lemma_names()[0],syn.lemma_names()[0],mer.definition()))
    for mer in syn.member_holonyms():
        print("Synset '{2}':\n\t{0}\n\nmember holonym '{1}':\n\t{3} ".format(syn.definition(),
              mer.lemma_names()[0],syn.lemma_names()[0],mer.definition()))
    for mer in syn.part_holonyms():
        print("Synset '{2}':\n\t{0}\n\npart holonym '{1}':\n\t{3} ".format(syn.definition(),
              mer.lemma_names()[0],syn.lemma_names()[0],mer.definition()))
    for mer in syn.substance_holonyms():
        print("Synset '{2}':\n\t{0}\n\nsubstance holonym '{1}':\n\t{3} ".format(syn.definition(),
              mer.lemma_names()[0],syn.lemma_names()[0],mer.definition()))

#8
from nltk.corpus import names
names.fileids()
tble=[(gender, first_letter) for gender in names.fileids() for first_letter in [w[0] for w in names.words(gender)]]
cfd=nltk.ConditionalFreqDist(tble)
cfd.plot()

#12

from nltk.corpus import cmudict
words=[a for a,b in cmudict.entries()]
len(set(words))-len(words)
i=0
m_words=words.copy()
for word in list(set(words)):
    print(i)
    i=i+1
    m_words.remove(word)
len(m_words)/len(words)
#13
from nltk.corpus import wordnet as wn
len(list(wn.all_synsets('n')))
no_hyph=[syn for syn in wn.all_synsets('n') if (not syn.hyponyms())]
len(no_hyph)/len(list(wn.all_synsets('n')))

#14
"""Define a function supergloss(s) that takes a synset s as its argument and returns
a string consisting of the concatenation of the definition of s , and the definitions
of all the hypernyms and hyponyms of s ."""

def supergloss(s):
    string=[]
    string.append(s.definition())
    string.append("\n\n")
    for hyper in s.hypernyms():
        string.append(hyper.definition())
        string.append("\n")
    string.append("\n")
    for hypo in s.hyponyms():
        string.append(hypo.definition())
        string.append("\n")
    return "".join(string)

print(supergloss(wn.synsets("car")[0]))

#15
"""Write a program to find all words that occur at least three times in the Brown
Corpus."""

from nltk.corpus import brown
from nltk import FreqDist
lbrown=[w.lower() for w in brown.words() if w.isalpha()]
fd=FreqDist(lbrown)
frequent_words=list(set([word for word in lbrown if fd[word]>=3]))

#16
"""Write a program to generate a table of lexical diversity scores (i.e., token/type
ratios), as we saw in Table 1-1. Include the full set of Brown Corpus genres
( nltk.corpus.brown.categories() ). Which genre has the lowest diversity (greatest
number of tokens per type)? Is this what you would have expected?"""
from nltk.corpus import brown
print("{0}:\t{1}\t{2}\t{3}\n".format("Category", "tokens", "word_types", "lexical diversity"))
for cat in brown.categories():
    tokens=len(brown.words(categories=cat))
    word_types=len(list(set([w.lower() for w in brown.words(categories=cat) if w.isalpha()])))
    print("{0:15s}:\t{1:6d}\t{2:6d}\t{3:5.2f}\n".format(cat, tokens, word_types, tokens/word_types))

#17
"""Write a function that finds the 50 most frequently occurring words of a text that
are not stopwords."""
from nltk import FreqDist
from nltk.corpus import stopwords, brown
def freq_no_stop(text, lan="english"):
    fd=FreqDist([w.lower() for w in text if not w.lower() in stopwords.words(lan) and w.isalpha()])
    sorted_keys=sorted(list(fd.items()), key=lambda el: -el[1])
    return [key for key, val in sorted_keys[:50]]
a=freq_no_stop(brown.words(categories='humor'))

#18
"""Write a program to print the 50 most frequent bigrams (pairs of adjacent words)
of a text, omitting bigrams that contain stopwords."""
from nltk import FreqDist
from nltk import bigrams
from nltk.corpus import stopwords, brown
def most_frequent_bigrams(text, lan="english"):
    bigrams_=[big for big in bigrams(text) if (not big[0] in
              stopwords.words(lan) and not big[1] in stopwords.words(lan) and big[0].isalpha() and big[1].isalpha())]
    fd=FreqDist(bigrams_)
    sorted_keys=sorted(list(fd.items()), key=lambda el: -el[1])
    print([key for key, val in sorted_keys[:50]])

most_frequent_bigrams(brown.words(categories='humor'))

#20
"""Write a function word_freq() that takes a word and the name of a section of the
Brown Corpus as arguments, and computes the frequency of the word in that sec-
tion of the corpus."""
from nltk.corpus import brown
brown.fileids()
def word_freq(word, name):
    return len([w for w in brown.words(categories=name) if w.lower()==word.lower()])

print(word_freq("was", 'humor'))

#21
"""Write a program to guess the number of syllables contained in a text, making
use of the CMU Pronouncing Dictionary."""

#I assume that number of syllables=number of 0s, 1s and 2s in the pronounciation
from nltk.corpus import cmudict

def n_syllables(sentence):
    entr=cmudict.dict()
    words=[word for word in sentence.replace('.','').replace(',','').split() if word.isalpha()]
    return sum([len([phon for phon in entr.get(word, 'a')[0] if [c for c in list(phon) if c.isdigit()]]) for word in words])

print(n_syllables(" ".join(brown.words(categories='romance')[:10])))
" ".join(brown.words(categories='romance')[:10])

#22
"""Define a function hedge(text) that processes a text and produces a new version
with the word 'like' between every third word."""

#I don't filter non-alpha word types, so '.' is treated as a word
import numpy as np
def hedge(text):
    l=len(text)
    return np.insert(np.array(text),list(range(3,l+1,3)),'like').tolist()

print(hedge(brown.words(categories='romance')[:100]))

#23
"""Zipf’s Law: Let f(w) be the frequency of a word w in free text. Suppose that all
the words of a text are ranked according to their frequency, with the most frequent
word first. Zipf’s Law states that the frequency of a word type is inversely
proportional to its rank (i.e., f × r = k, for some constant k). For example, the 50th
most common word type should occur three times as frequently as the 150th most
common word type."""

from nltk import FreqDist
from nltk.corpus import brown
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import linregress
from math import exp
import random
def check_zipf_law(text):
    fd=FreqDist(text)
    sorted_items=sorted(list(fd.items()), key=lambda el: -el[1])
    rank=np.array(range(1,len(sorted_items)+1,1))
    log_rank=np.log(rank)
    log_freq=np.log(np.array([freq for word, freq in sorted_items]))
    plt.figure()
    plt.plot(log_rank, log_freq)
    slope, intercept, r_value, p_value, std_err = linregress(log_rank,log_freq)
    print("To confirm Zipf's law, the slope of the plot should be equal to -1.\nIt is equal to {0:3.1f}.\nThe constant k is equal to {1:3.1f}.".format(slope, exp(intercept),))
    plt.show()

check_zipf_law(brown.words())

random_text="".join([random.choice('abcdefghijklmn ') for i in range(0,10000000)]).split(" ")
check_zipf_law(random_text)

#24
"""Modify the text generation program in Example 2-1 further, to do the following
tasks:
a. Store the n most likely words in a list words , then randomly choose a word
from the list using random.choice() . (You will need to import random first.)
b. Select a particular genre, such as a section of the Brown Corpus or a Genesis
translation, one of the Gutenberg texts, or one of the Web texts. Train the
model on this corpus and get it to generate random text. You may have to
experiment with different start words. How intelligible is the text? Discuss the
strengths and weaknesses of this method of generating random text.
c. Now train your system using two distinct genres and experiment with gener-
ating text in the hybrid genre. Discuss your observations."""
from nltk import bigrams
from nltk import ConditionalFreqDist
def generate_model(cfdist, word, num=15, n_most_likely=5):
    for i in range(num):
        print(word, end=' ')
        sorted_items=sorted(list(cfdist[word].items()), key=lambda el: -el[1])[:max([n_most_likely, len(cfdist[word].items())])]
        l1=[word for word,val in sorted_items]
        word=random.choice(l1)
    print(' ')
brown.categories()
bigram=bigrams([word for word in brown.words(categories=['government', 'mystery']) if word.isalpha()])
cfd=ConditionalFreqDist(bigram)
cfd["I"].items()
generate_model(cfd, 'I', num=25, n_most_likely=6)

#25
"""Define a function find_language() that takes a string as its argument and returns
a list of languages that have that string as a word. Use the udhr corpus and limit
your searches to files in the Latin-1 encoding."""
from nltk.corpus import udhr
[file for file in udhr.fileids() if 'Latin1' in file]
from nltk import ConditionalFreqDist

def find_language(string):
    text=string.split(" ")
    text=[word for word in text if word.isalpha()]
    l=len(text)
    avail_langs=[file for file in udhr.fileids() if 'Latin1' in file]
    cfd=ConditionalFreqDist([(lang, word) for lang in avail_langs for word in [word for word in text if word in udhr.words(lang)]])
    ls=sorted([(lang,cfd[lang]) for lang in avail_langs], key=lambda tple: tple[1].N())
    print("The most probable language of the text is {0} with {1:3.3f}% probability.".format(ls[-1][0].replace('-Latin1',''), 100*ls[-1][1].N()/l))

find_language(" ".join(udhr.words('Danish_Dansk-Latin1')[:20]))

#expected wrong results because Polish is not in the udhr corpus
find_language('Temistokles Brodowski z wydziału komunikacji społecznej biura potwierdził dziś, że agenci z katowickiej delegatury CBA zatrzymali byłego ministra sprawiedliwości, radcę prawnego Andrzeja K., jego współpracownika z kancelarii Piotra K. oraz gdańskiego biznesmena Marka S. i byłego funkcjonariusza Wojskowych Służb Informacyjnych Jerzego K. Andrzej K. był szefem resortu sprawiedliwości w drugim rządzie Marka Belki.')

#lets try french
find_language("Solidaire du mouvement des cheminots et outré par « le manque de dialogue social », Nicolas, ingénieur informatique naviguant entre Paris et Caen, parvient lui aussi à s’organiser en recourant au télétravail. « Les jours de grève, finalement tout le monde est chez soi, on travaille par “conf call” et on ne prend pas de rendez-vous », détaille-t-il.")

#26
"""What is the branching factor of the noun hypernym hierarchy? I.e., for every
noun synset that has hyponyms—or children in the hypernym hierarchy—how
many do they have on average? You can get all noun synsets using wn.all_syn
sets('n') ."""

from nltk.corpus import wordnet
hyponyms=[len(item.hyponyms()) for item in list(wordnet.all_synsets('n')) if item.hyponyms()]
sum(hyponyms)/len(hyponyms)

#27
"""The polysemy of a word is the number of senses it has. Using WordNet, we can
determine that the noun dog has seven senses with len(wn.synsets('dog', 'n')) .
Compute the average polysemy of nouns, verbs, adjectives, and adverbs according
to WordNet."""

from nltk.corpus import wordnet
all_nouns=list(set([synset._lemma_names[0] for synset in wordnet.all_synsets(pos=wordnet.NOUN)]))
all_verbs=list(set([synset._lemma_names[0] for synset in wordnet.all_synsets(pos=wordnet.VERB)]))
all_adj=list(set([synset._lemma_names[0] for synset in wordnet.all_synsets(pos=wordnet.ADJ)]))
all_adv=list(set([synset._lemma_names[0] for synset in wordnet.all_synsets(pos=wordnet.ADV)]))
pol_noun=[len(wordnet.synsets(syn, 'n')) for syn in all_nouns]
pol_verb=[len(wordnet.synsets(syn, pos=wordnet.VERB)) for syn in all_verbs]
pol_adv=[len(wordnet.synsets(syn, pos=wordnet.ADV)) for syn in all_adv]
pol_adj=[len(wordnet.synsets(syn, wordnet.ADJ)) for syn in all_adj]
whole=[sum(pol_noun)/len(pol_noun), sum(pol_verb)/len(pol_verb),sum(pol_adv)/len(pol_adv),sum(pol_adj)/len(pol_adj)]
labels=['noun', 'verb', 'adverb', 'adjective']
for i in range(len(labels)):
    print("The average polisemy for {0} is equal to {1:4.2f}.".format(labels[i], whole[i]))


#28
"""Use one of the predefined similarity measures to score the similarity of each of
the following pairs of words. Rank the pairs in order of decreasing similarity. How
close is your ranking to the order given here, an order that was established exper-
imentally by (Miller & Charles, 1998): car-automobile, gem-jewel, journey-voyage,
boy-lad, coast-shore, asylum-madhouse, magician-wizard, midday-noon, furnace-
stove, food-fruit, bird-cock, bird-crane, tool-implement, brother-monk, lad-
brother, crane-implement, journey-car, monk-oracle, cemetery-woodland, food-
rooster, coast-hill, forest-graveyard, shore-woodland, monk-slave, coast-forest,
lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string."""

from nltk.corpus import wordnet as wn
text="car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore, asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock, bird-crane, tool-implement, brother-monk, lad-brother, crane-implement, journey-car, monk-oracle, cemetery-woodland, food-rooster, coast-hill, forest-graveyard, shore-woodland, monk-slave, coast-forest, lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string"
text=text.replace(',', '')
text=text.split(' ')
pairs=[item.split('-') for item in text]
similarities=[min([wn.synsets(pairs[k][0])[i].path_similarity(wn.synsets(pairs[k][1])[j]) for i in range(len(wn.synsets(pairs[k][0]))) for j in range(len(wn.synsets(pairs[k][1]))) if type(wn.synsets(pairs[k][0])[i].path_similarity(wn.synsets(pairs[k][1])[j]))!=type(wn.synsets(pairs[0][0])[0].path_similarity(wn.synsets(pairs[0][1])[1]))]) for k in range(len(pairs))]
print(sorted([(pairs[i], similarities[i]) for i in range(len(pairs))], key=lambda x: x[1], reverse=True))