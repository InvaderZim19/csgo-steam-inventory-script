import urllib2
import json
import sys
import os.path
import datetime
import time

def createInventoryFile(steamid, botNumber):
	print('Writing file...')

	data = urllib2.urlopen('http://steamcommunity.com/profiles/'+steamid+'/inventory/json/730/2')
	json_data = json.loads(data.read())
	descriptions = json_data['rgDescriptions']
	items = []
	for v in descriptions:
		items.append([descriptions[v]['name'], descriptions[v]['descriptions']])
	
	# enter items here
	itemSearch = ['device', 'katowice2014']

	findItems('bot' + botNumber + '.txt', items, itemSearch)

	# time.sleep(cycleTime)

def findItems(file, items, searchItems):
	print('Finding items...')
	now = datetime.datetime.now()

	file = open("bot1.txt", 'w')

	matches = []

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


createInventoryFile('76561197998202248', '1')




	# http://steamcommunity.com/profiles/76561197998202248/inventory/json/730/2
	