import feedparser
import argparse
import os
import json
import hashlib
import time
import urllib2
import shelve
import urllib2

from cache import *

app_home = os.path.expanduser("~")+'/.newsreader/'

def build_config():
	parser = argparse.ArgumentParser()
	parser.add_argument	("-a",	help="add rss feed")
	parser.add_argument("-u", help="update feeds")
	args = parser.parse_args()
	return args

def get_diff(newtime,oldtime,seconds=14400):
	s = newtime-oldtime
	if newtime-oldtime > seconds:
		return True
	else:
		return False
			
def get_md5(string):
	m  = hashlib.md5('string')
	return m.hexdigest()		
	

	

	
def add_feed(feed):
	
	if not os.path.exists(app_home):
		os.makedirs(app_home)
	
	f = open(h+'feeds', 'a')
	
	f.write(feed+'\n')
	f.close()
	return


def main():
	
	
	if args.a:
		add_feed(args.a)
	elif args.u:
		pass

	





		
		

				

		

	
