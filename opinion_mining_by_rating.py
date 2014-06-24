#!/usr/bin/python

#read part-m- files
def classifier():
	file_list = ['part-m-00000','part-m-00001','part-m-00002','part-m-00003','part-m-00004','part-m-00005','part-m-00006','part-m-00007','part-m-00008']
	for flist in file_list:
		with open('review_rating/' + flist) as f:
			for line in f:
				cols = line.split(':')
				business_id = cols[0]
				rating = cols[1]
				sentence = cols[2]
				category = 0
				if int(rating) < 3:
					category = -1
				elif int(rating) == 3:
					category = 0
				else:
					category = 1
				print business_id + " : " + str(category) + " : "  + sentence.strip()
				

#main method
if __name__ == "__main__":
	classifier()
