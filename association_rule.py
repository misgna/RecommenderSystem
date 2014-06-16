#!/usr/bin/python
fList = {}
# create dictionary
def tags_frequency_dict():
	with open('business_and_tags/fList.txt') as f:
		for line in f:
			if "Key: " in line:
				cols = line.split(':')
				fList[cols[1].strip()] = cols[3].strip()

# association rule definition
def association_rule():
	with open('business_and_tags/frequentpatterns.txt') as f:
		for line in f:
			if "Key: " in line:
				cols = line.split(':')
				lhs = cols[1].strip()
				num_rhs = cols[3].count("([")
				pre_rhs = cols[3].split("), (")
				for index in range(0, int(num_rhs)):
					rhs = pre_rhs[index].split('],')[0].replace(lhs, '').replace('(','').replace('[','')
					freq = pre_rhs[index].split('],')[1].replace(')','')
					sup = float(freq)/float(number_of_business)
					con = float(freq)/float(fList[lhs])
					if rhs.strip():
						print lhs + ' -->' + rhs + '  :: sup = ' + str(sup) + ', con = ' + str(con)	

#read business and tags

#main method
if __name__ == "__main__":
	tags_frequency_dict()
	association_rule()
