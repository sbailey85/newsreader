import feedparser
import argparse
import os
import json
from hashlib import md5
import time
import urllib2

parser = argparse.ArgumentParser()
parser.add_argument	("-a",	help="add rss feed")
parser.add_argument("-u", help="update feeds")


args = parser.parse_args()
app_home = os.path.expanduser("~")+'/.newsreader/'
class ParseCache:
	def __init__(self,max_age=14400):
		pass
		
class GetCache:
	def __init__(self,feedlink,age=0):
		has = md5()
		has.update(feedlink)
		cache_dir = h+"cache/"+has.digest()
		if os.path.exists(cache_dir) :
			pass
		now = time.time()
		f  = open(cache_dir, 'w')
		f.write(urlib2.urlopen(feedlink).read())
		f.close()
		
		
			


def fp(url):
	li  = []
	p = feedparser.parse(url)
	final = {}
			
	
	for x in p['items']:
		z = x['link']
		desc = x['description']
		o =  {'title': z ,'description': desc}
		self.d[z] = o
	
		
	return d		
		

def add_feed(feed):
	
	if not os.path.exists(app_home):
		os.makedirs(app_home)
	
	f = open(h+'feeds', 'a')
	
	f.write(feed+'\n')
	f.close()
	return




if args.a:
	add_feed(args.a)
elif args.u:
	pass
	
	




	

class Termnews:
	def __init__(self,url):
		self.d = {}
		self.sep = ':'

		
		
		
	def disp(self):
		for x in self.d.keys():
			print(x+self.sep+self.d[x])
	def get_keys(self):
		return self.d.keys()
		

		
		
		
		
				

		

		
