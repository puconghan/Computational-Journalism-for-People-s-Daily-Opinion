#encoding=utf-8
import jieba
import jieba.analyse
import csv

jieba.load_userdict("customized_dict.txt")

TFIDF = []
all_text = ""
reader = csv.reader(open("results/segmentation-jieba-result.csv", "rb"))
for line in reader:
	for word in line:
		all_text = all_text + word
for item in jieba.analyse.extract_tags(all_text, 20):
		TFIDF.append(item.encode('utf-8'))

with open("results/tfidf-jieba-all-result.csv", 'w') as f:
	writer = csv.writer(f)
	writer.writerow(TFIDF)