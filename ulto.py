#!/usr/local/bin/python3

import urllib.request as Request
import subprocess
import re
import sys

if __name__ == '__main__':

	if(sys.argv.__len__()<2):
		print('Please speficied the URL.')
		exit()
	else:
		URL = sys.argv[1]
	
	with open('conf','r') as f:
		HOST = str(sys.argv[0].split('.')[0])
		while(f.readline().rstrip() != HOST):
			True
		USERandPASS = f.read().rstrip()
		
	with Request.urlopen(URL) as f:
		pattern = '(?<=<title>).*(?= \(.*\) - uploaded.net</title>)'
		fileTitle = re.findall(pattern, str(f.read(500)))[0]

	subprocess.call('exec echo '+fileTitle, shell=True)
#	subprocess.call('exec plowdown --auth='+USERandPASS+' '+URL+' > /dev/null &', shell=True)