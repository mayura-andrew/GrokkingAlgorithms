#phone_book = dict()
#or
# python dictionary == hash tabels
# key and value pair

phone_book = {}

phone_book["jenny"] = 898343
phone_book["emergency"] = 911

print(phone_book["jenny"])
print(phone_book["emergency"])


voted = {}

def check_voter(name):
	if voted.get(name):
		print("kick them out")
	else:
		voted[name] = True
		print("Let them vote")


check_voter("mike")
check_voter("tom")
check_voter("tom")


# Simple cache 

cache = {}

def get_page(url):
	if cache.get(url):
		return cache[url]
	else:
		data = get_data_from_server(url)
		cache[url] = data
		return data


# hashes are good fore

''' 
modeling relationships from one thing to another thing
filtering out duplicates
caching/memorizing data instead of making your server do work

Average case of hash - O(1)  constant time

      hash tables hash tables Arrays Linked Lists 
       (avarage)    (worst)
search O(1)         O(n)        O(1)     O(n)
insert O(1)         O(n)        O(n)     O(1) 
delete O(1)         O(n)        O(n)     O(1)
'''
