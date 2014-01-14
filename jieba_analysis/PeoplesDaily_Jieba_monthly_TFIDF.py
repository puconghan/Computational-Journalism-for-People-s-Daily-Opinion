#encoding=utf-8
import jieba
import jieba.analyse
import csv

jieba.load_userdict("customized_dict.txt")

TFIDF = []
reader = csv.reader(open("results/segmentation-jieba-result.csv", "rb"))
for line in reader:
	all_text = ""
	line_list = []
	for word in line:
		all_text = all_text + word
	for item in jieba.analyse.extract_tags(all_text, 10):
		line_list.append(item.encode('utf-8'))
	TFIDF.append(line_list)

with open("results/tfidf-jieba-monthly-result.csv", 'w') as f:
	writer = csv.writer(f)
	writer.writerows(TFIDF)