import string
import csv
import fileinput
import array
import numpy
from operator import itemgetter

NUM = 20
sumlist = numpy.zeros(38390)
lists = []
resultlist = []
with open('resultlist/gensim_TFIDF.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		for word in row:
			sumlist[int(word[word.find("(")+1:word.find(",")])] = sumlist[int(word[word.find("(")+1:word.find(",")])] + float(word[word.find(",")+1:word.find(")")])

count = 0
for item in sumlist:
	lists.append([count, item])
	count += 1
sortedlist = sorted(lists, key=itemgetter(1), reverse=True)

for i in range(0,NUM-1):
	resultlist.append(sortedlist[i])
	
with open('PeoplesDaily_gensim_dic.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		for item in resultlist:
			if str(item[0]) == str(row[0]):
				item[0] = str(row[1])
print resultlist
w = csv.writer(open("resultlist/gensim_TFIDF_word.csv", "wb"))
w.writerows(resultlist)
		
