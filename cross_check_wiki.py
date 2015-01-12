import urllib2

def loadFile():
	with open('aspects_100') as f:
		for line in f:
			line = line.replace('(','').replace(')\n','').replace('\'','')
			cols = line.split(',')
			if isFood(cols[0]) == 'food':
				print cols[0]
def isFood(item):
	try:
		description = urllib2.urlopen('https://en.wikipedia.org/wiki/' + item)
		text = remove_tags(description.read())
		text = text.split(' ')
		if 'food' in text or 'foods' in text or 'drink' in text or 'drinks' in text or 'dish' in text or 'dishes' in text:
			return 'food'
	except urllib2.HTTPError as e:
		print e.code
		#print e.read()

def remove_tags(text):
    	#return ''.join(xml.etree.ElementTree.fromstring(text).itertext()
	return text
if __name__ == "__main__":
	loadFile()
else:
	print 'method is not called'
