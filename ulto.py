#!/usr/local/bin/python3

import urllib.request as Request
import subprocess
import re
import sys
#print()
if __name__ == '__main__':
	if(sys.argv.__len__()<2):
		print('Please speficied the URL.')
		exit()
	
	URL = sys.argv[1]

	with open('conf','r') as f:
		USERandPASS = f.read()
	
	with Request.urlopen(URL) as f:
		pattern = '(?<=<title>).*(?= \(.*\) - uploaded.net</title>)'
		fileTitle = re.findall(pattern, str(f.read(500)))[0]

	subprocess.call('exec echo '+fileTitle, shell=True)
	subprocess.call('exec echo '+USERandPASS, shell=True)
#	subprocess.call('exec plowdown --auth='+USERandPASS+' '+URL+' > /dev/null &', shell=True)