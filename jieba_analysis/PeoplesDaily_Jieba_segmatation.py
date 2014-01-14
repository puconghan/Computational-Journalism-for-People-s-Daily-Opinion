#encoding=utf-8
import os
import glob
import jieba
import jieba.analyse
import csv

segList = []
raw_data_path = 'monthly_raw_data/'
file_name = ["201010", "201011", "201012", "201101", "201103", "201105", "201107", "201109", "201110", "201111", "201112", "201201", "201202", "201203", "201205", "201206", "201208", "201210", "201211"]

jieba.load_userdict("customized_dict.txt")

for name in file_name:
	all_text = ""
	multi_line_text = ""
	with open(raw_data_path + name + ".txt", "r") as file:
		for line in file:
			if line != '\n':
				multi_line_text += line
		templist = multi_line_text.split('\n')
		for text in templist:
			all_text += text
		seg_list = jieba.cut(all_text,cut_all=False)
		temp_text = []
		for item in seg_list:
			temp_text.append(item.encode('utf-8'))
		
		stop_list = []
		with open("stopwords.txt", "r") as stoplistfile:
			for item in stoplistfile:
				stop_list.append(item.rstrip('\r\n'))
		
		text_without_stopwords = []
		for word in temp_text:
			if word not in stop_list:
				text_without_stopwords.append(word)
		
		segList.append(text_without_stopwords)

with open("results/segmentation-jieba-result.csv", 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(segList)
		
		