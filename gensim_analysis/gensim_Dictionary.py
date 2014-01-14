#encoding=utf-8
import re
import urllib2
import string
import csv
import fileinput
from gensim import corpora, models, similarities

diclist = []
texts = []
with open('segmentation-jieba-result.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		for word in row:
			texts.append(word)
dictionary = corpora.Dictionary(line.split() for line in texts)
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(once_ids)
dictionary.compactify()

valuelist = dictionary.token2id.values()
keylist = dictionary.token2id.keys()

for item in range(0, len(dictionary)):
	diclist.append([valuelist[item], keylist[item]])
#print diclist
w = csv.writer(open("PeoplesDaily_gensim_dic.csv", "wb"))
w.writerows(diclist)
	
	

corpus1012 = []
with open('segmentation-jieba-result.csv','rU') as ff:
	reader2 = csv.reader(ff)
	for row2 in reader2:
		corpus1012.append(row2)
class MyCorpus(object):
	def __iter__(self):
		for line in corpus1012:
			yield dictionary.doc2bow(line)

corpus_memory_friendly = MyCorpus()
print corpus_memory_friendly
for vector in corpus_memory_friendly:
	print vector

corpora.MmCorpus.serialize('corpus.mm', corpus_memory_friendly)


