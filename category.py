#!/usr/bin/python

#define the five classes
restaurants = ['restaurants', 'nightlife', 'sandwiches', 'brunch',  'american (traditional)', 'american (new)', 'pizza', 'fast food',' mexican, bars', 'chinese', 'sports bars', 'breakfast', 'mediterranean', 'japanese', 'delis', 'tex-mex', 'chicken wings', 'salad', 'buffets', 'barbeque', 'asian fusion', 'bagels', 'steakhouses', 'diners', 'sushi bars', 'hot dogs', 'burgers', 'lounges']

entertainment = ['entertainment', 'arts', 'music venues', 'performing arts', 'cinema', 'art galleries', 'festivals', 'arenas', 'stadiums', 'blues', 'arcades', 'wineries', 'casinos']

accomodation = ['travel', 'hotels', 'services', 'event planning', 'event spaces', 'venues', 'resorts', 'breakfast', 'bed', 'hot air balloons', 'horseback riding', 'campgrounds']

sport = ['gyms', 'fitness', 'instruction', 'trainers', 'boot camps', 'sports clubs']
transport = ['transportation','airport shuttles','taxis', 'limos','airlines','public transportation']

def category():
	with open('business_id_tags/part-m-00000') as f:
		for line in f:
			cols = line.split(':')
			business_id = cols[0].strip()
			pre_tags = cols[1].strip().replace('[', '').replace(']', '').replace('"','')
			tags = pre_tags.split(',')
			
			#store the intersection values of tags from the file and business defined
			result_restaurant = list(set(tags) & set(restaurants))
			result_entertainment = list(set(tags) & set(entertainment))
			result_accomodation = list(set(tags) & set(accomodation))
			result_sport = list(set(tags) & set(sport))
			result_transport = list(set(tags) & set(transport))
	

			if result_restaurant:
				print business_id + ' : restaurant'
			elif result_entertainment:
				print business_id + ' : entertainment'
			elif result_accomodation:
				print business_id + ' : accomodation'
			elif result_sport:
				print business_id + ' : sport'
			elif result_transport:
				print business_id + ' : transport'


#main method
if __name__ == "__main__":
	category()
