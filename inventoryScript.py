import urllib2
import json
import sys
import os.path
import datetime
import time

def createInventoryFile(steamid, botNumber):
	print('Writing file...')

	# this is the json query, it reads each of the items from the inventory
	# and then puts it into a list
	data = urllib2.urlopen('http://steamcommunity.com/profiles/'+steamid+'/inventory/json/730/2')
	json_data = json.loads(data.read())
	descriptions = json_data['rgDescriptions']
	items = []
	for v in descriptions:
		items.append([descriptions[v]['name'], descriptions[v]['descriptions']])
	
	# enter items you are looking for here, in lowercase
	# ex: itemSearch = ['katowice2014', 'dignitas']
	itemSearch = ['device', 'katowice2014']

	findItems('bot' + botNumber + '.txt', items, itemSearch, botNumber)

def findItems(file, items, searchItems, botNumber):
	print('Finding items...')

	# creating current time
	now = datetime.datetime.now()

	# opening the file containing all the items matched
	file = open('bot' + botNumber + '.txt', 'w')

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

	print ('Finished! ' + str(datetime.datetime.now()) + ' Bot ' + botNumber)


# this actually runs it, the first perameter changes the ID that you want

# So I counted 18 bots so I made 18 separate files, designed to match each of the bots
# Just plug in the ID's of the bots above inbetween the single quotes

createInventoryFile('', '1')
createInventoryFile('', '2')
createInventoryFile('', '3')
createInventoryFile('', '4')
createInventoryFile('', '5')
createInventoryFile('', '6')
createInventoryFile('', '7')
createInventoryFile('', '8')
createInventoryFile('', '9')
createInventoryFile('', '10')
createInventoryFile('', '11')
createInventoryFile('', '12')
createInventoryFile('', '13')
createInventoryFile('', '14')
createInventoryFile('', '15')
createInventoryFile('', '16')
createInventoryFile('', '17')
createInventoryFile('', '18')

# ignore this
# http://steamcommunity.com/profiles/76561197998202248/inventory/json/730/2
	