import feedparser
import argparse
import os
import json
import hashlib
import time
import urllib2
import shelve
import urllib2

from newsreader.Cache import GetCache

app_home = os.path.expanduser("~")+'/.newsreader/'

def build_config():
    parser = argparse.ArgumentParser()
    parser.add_argument ("-a",  help="add rss feed")
    parser.add_argument("-u", help="update feeds")
    args = parser.parse_args()
    return args


            
        
    
def add_feed(feed):
    
    if not os.path.exists(app_home):
        os.makedirs(app_home)
    
    f = open(h+'feeds', 'a')
    
    f.write(feed+'\n')
    f.close()
    return

c = GetCache('http://www.infowars.com/feed/custom_feed_rss')


    





        
        

                

        

    
