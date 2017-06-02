#simple app that lets youcheck out the contents of a JSON file.

import json

def getJson(filename):
	fn = '/home/sean/GitHub/FunPython/' + filename
	jsonTxt = ''
	f = open(fn)
	for line in f:
		line = line.strip()
		jsonTxt = jsonTxt + line
	ret = json.loads(jsonTxt)
	return ret

def getKeys(dict):
	keyList = ''
	keysRaw = dict.keys()
	for k in keysRaw:
		keyList = keyList + k + ', '
	#cut off the last comma and space
	keyList = keyList[:-2]
	return keyList

def getValues(key, contents):
	ret = ''
	for d in contents:
		for item in d[key]:
			ret = ret + item + ', '
	#cut off the last comma and space
	ret = ret[:-2]
	return ret

def main():
	print 'enter the filename of your json file: ',
	file = raw_input()
	contents = getJson('albums.json')
	keys = getKeys(contents[0])
	print 'The keys in the JSON file are:' + keys
	print 'which key do you want to peruse? ',
	k = raw_input()
	print getValues(k, contents)

main()