#encoding=utf-8
import re
import urllib2
import string
import csv
from gensim import corpora, models, similarities

PeoplesDaily = []

corpus = corpora.MmCorpus('corpus.mm')
tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
	PeoplesDaily.append(doc)
with open("resultlist/gensim_TFIDF.csv", 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(PeoplesDaily)
print "TFIDF Complete"