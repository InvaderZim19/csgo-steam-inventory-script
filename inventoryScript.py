import urllib2
import json
import sys
import os.path
import datetime
import time

def createInventoryFile(steamid, botNumber):
	print('Writing file...')

	# this is the json query, it reads each of the items from the inventory
	data = urllib2.urlopen('http://steamcommunity.com/profiles/'+steamid+'/inventory/json/730/2')
	json_data = json.loads(data.read())
	descriptions = json_data['rgDescriptions']
	items = []
	for v in descriptions:
		items.append([descriptions[v]['name'], descriptions[v]['descriptions']])
	
	# enter items here, in lowercase
	itemSearch = ['device', 'katowice2014']

	findItems('bot' + botNumber + '.txt', items, itemSearch)

def findItems(file, items, searchItems):
	print('Finding items...')

	# creating current time
	now = datetime.datetime.now()

	# opening the file containing all the items matched
	file = open("bot1.txt", 'w')

	matches = []

	# for each item, if any of the items contain the items listed
	# then print it onto the file
	for s in searchItems:
		matches.append([i for i in items if s in str(i)])
	
	for m in matches:
		file.write("%s\n" % m)

	print matches

	file.write('')
	file.write(str(now) + ' createFile')
	file.write('')
	file.close()

	print ('Finished! ' + str(datetime.datetime.now()))


# this actually runs it, the first perameter changes the ID that you want
# the second perameter just leave it.
createInventoryFile('76561197998202248', '1')




	# http://steamcommunity.com/profiles/76561197998202248/inventory/json/730/2
	