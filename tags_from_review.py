#!/usr/bin/python

from nltk.corpus import stopwords
stop = stopwords.words('english')

def features():
	file_list = ['part-m-00000','part-m-00001','part-m-00002','part-m-00003','part-m-00004','part-m-00005','part-m-00006','part-m-00007','part-m-00008']
	for flist in file_list:
		with open('review_rating/' + flist) as f:
			for line in f:
				cols = line.split(':')
				business_id = cols[0]
				rating = cols[1]
				sentence = cols[2].lower()
				print (business_id, rating, [i for i in sentence.split() if i not in stop])
				

#main method
if __name__ == "__main__":
	features()
