
# coding: utf-8

# In[302]:

# read sentences from file "Building_Global_Community.txt"
# read it as a whole sentences

text = open('building_global_community-.txt').read()


# In[331]:

# split sentences into words (split, or nltk word_tokenize from nltk)

import nltk
nltk.download('punkt')
from nltk import wordpunct_tokenize
words = wordpunct_tokenize(text)
len(words)


# In[332]:

#filter out symbols (isalpha, isdigit, isalnum)
# use "not any" which remove the words include isdigit, isalnum"

wordsTwo =[x for x in words if not any(c.isdigit() for c in x )]
len(wordsTwo)


# In[334]:

# remove the only one alpha
wordsThree = [word for word in wordsTwo if word.isalpha() is True]
len(wordsThree)


# In[333]:

wordsThree


# In[311]:

# normalize words ('Word' and 'word' are considered as the same word)

wordsFour = [element.lower() for element in wordsThree]


# In[335]:

# filter out stopwords (stopwords from nltk)

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))


# In[336]:

# remove the stopwords
wordsFive = [word for word in wordsFour if word not in stopwords]
len(wordsFive)


# In[316]:

wordsFive


# In[337]:

#count the occurance of words (Counter)

from collections import Counter
counterwordsFive = Counter(wordsFive)
counterwordsFive


# In[320]:

counterwordsFive.most_common(20)


# In[340]:

wordsSix =nltk.pos_tag(wordsFive)


# In[339]:

# The result probably looks like this: VERB: {play: 100, go: 23, do: 15, ...}, NOUN: {community: 80, government: 52, school: 35, ...},

tag_fdTwo =nltk.FreqDist(tag for tag in wordsSix)
tag_fdTwo


# In[326]:

import csv


# In[329]:

with open('Dobby_wordcount2.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for word, count in counterwordsFive.most_common(20):
        writer.writerow({'word': word, 'count': count})

