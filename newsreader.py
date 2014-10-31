import feedparser
import argparse
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument	("-a",	help="add rss feed",)

args = parser.parse_args()



		

def add_feed(feed):
	h = os.path.expanduser("~")+'/.newsreader/'
	if not os.path.exists(h):
		os.makedirs(h)
	
	f = open(h+'feeds', 'a')
	
	f.write(feed+'\n')
	f.close()
	return




if args.a:
	add_feed(args.a)




	

class Termnews:
	def __init__(self,url):
		self.d = {}
		self.sep = ':'
		def fp(self,url):
			li  = []
			p = feedparser.parse(url)
			final = {}
			
	
			for x in p['items']:
				z = x['title']
				p = x['link']
				self.d[z] = p
	
		
			return self.d
		fp(self,url)
		
		
	def disp(self):
		for x in self.d.keys():
			print(x+self.sep+self.d[x])
		
		
		
		
				
		
		

		
