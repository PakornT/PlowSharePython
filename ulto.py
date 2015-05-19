#!/usr/local/bin/python3

import urllib.request as Request
import re
#print()
with Request.urlopen('http://uploaded.net/file/u5bq81z6') as f:
	pattern = '(?<=<title>).*(?= \(.*\) - uploaded.net</title>)'
	fileTitle = re.findall(pattern, f.read(300))
#	print(fileTitle)