#!/usr/bin/python
import nltk

#read part-m- files
positive = []
negative = []
countPos = 0
countNeg = 0
def loadPosNeg():
	#load negative words into a list
	with open('dataset/negative-words','r') as fneg:
		for line in fneg:
			if not  (line.startswith(";") or line.startswith(" ")):
				negative.append(line.replace("\n",""))
	fneg.closed
	#load positive words into a list
	with open('dataset/positive-words', 'r') as fpos:
		for line in fpos:

			if not  (line.startswith(";") or line.startswith(" ")):
				positive.append(line.replace("\n",""))
	fpos.closed
	
def classifier():
	file_list = ['part-m-00000','part-m-00001','part-m-00002','part-m-00003','part-m-00004'
			,'part-m-00005','part-m-00006','part-m-00007','part-m-00008']

	numOfSimilarRating = 0
	numOfReviews = 0
	accuracy = 0

	

	for flist in file_list:
		with open('review_rating/' + flist) as f:
			for line in f:
				cols = line.split(':')
				business_id = cols[0]
				rating = cols[1]
				sentence = cols[2].lower()
				text = nltk.word_tokenize(sentence)
				posCount = len(list(set(positive) & set(text)))
				negCount = len(list(set(negative) & set(text)))

				if int(posCount) < int(negCount):
					category = -1
				elif int(posCount) >= int(negCount):
					category = 1
				
				#counting similar ratings
				if(int(category) == int(ratingClass(rating))):
					numOfSimilarRating += 1
				numOfReviews += 1



	accuracy = float(numOfSimilarRating)/numOfReviews

	print "Total number of reviews : " + str(numOfReviews)
	print "Total similar rating : " +str(numOfSimilarRating)
	print "The accuracy is : " + str(accuracy)
	print "Number of positive ratings : " + str(countPos)
	print "Number of negative ratings : " + str(countNeg)
				
				#print business_id + " : " + str(category) + " : " + str(rating)
				
def ratingClass(rating):
	global countPos
	global countNeg 
	if int(rating) >= 3:
		countPos += 1
		return 1
	elif int(rating) <= 2:
		countNeg += 1
		return -1

#main method
if __name__ == "__main__":
	loadPosNeg()
	classifier()
