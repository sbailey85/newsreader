#!/usr/bin/python2.7
#""" Caching module """
import shelve
import logging
import os
import hashlib
import time
import urllib2
app_home = os.path.expanduser("~")+'/.newsreader/'
import json
import feedparser
def get_md5(string):
    m  = hashlib.md5('string')
    return m.hexdigest()

def get_diff(newtime,oldtime,seconds=14400):
    s = newtime-oldtime
    if newtime-oldtime > seconds:
        return True
    else:
        return False



def fp(url):
    li  = []
    p = feedparser.parse(url)
    final = {}
    d = {}

    for x in p['items']:
        z = x['link']
        desc = x['description']
        o =  {'title': z ,'description': desc}
        d[z] = o




    return d

class GetCache:
    def __init__(self,feedlink,cache_dir=None):
        if not cache_dir ==  None:
            cache_dir = cache_dir

        cache_dir = app_home+"cache/"+get_md5(feedlink)
        self.cache_dir = app_home+"cache/"+get_md5(feedlink)
        body_cache = self.cache_dir+'.body'
        def update_json(feedlink):


            #del d[key]
            a = fp(feedlink)
            logging.warning(type(a))
            json.dump(a,open(cache_dir, 'w'))
            logging.warning('dumping json to '+self.cache_dir)

            return True



        if not os.path.exists(app_home+"cache/"):
            os.makedirs(app_home+"cache/")
        #d = shelve.open(self.cache_dir)
        if os.path.exists(self.cache_dir):
            logging.warning('old file')

            self.d = json.load(open(cache_dir))
            logging.warning('hi')



        else:

            #d = shelve.open(self.cache_dir)
            #print(d.keys())
            #f = d[self.cache_dir]
            logging.warning('need new file')
            update_json(feedlink)
            self.d = json.load(open(cache_dir))




        def cache_url():
            openurl = urllib2.urlopen(feedlink)
            out = open(self.cache_dir+'.body','w')
            out.write(openurl.read())
            out.close()
            return True




        #if os.path.exists(self.cache_dir) and os.path.exists(body_cache) :
            #d = json.load(open(self.cache_dir))
            ##f = open(cache_dir+'.body')
            ##if get_diff(time.time(), d[self.cache_dir]['time']):
                ##d[self.feedurl] = {'time': time.time(),
                ##'url': feedlink}
                ##logging.warning('logging url')
                ##cache_url()







        #else:



            get_url = urllib2.urlopen(feedlink)
            d = {}
            d[self.cache_dir] = {'time': time.time(),
            'url': feedlink}

            f  = open(self.cache_dir+'.body', 'w')
            f.write(urllib2.urlopen(feedlink).read())

            f.close()
            update_json(feedlink)




        #self.li = d[self.cache_dir]['url']
        #self.ti = d[self.cache_dir]['time']



