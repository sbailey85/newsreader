#!/usr/bin/python2.7
#""" Caching module """
import shelve

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
	self.d = shelve		
	
	for x in p['items']:
		z = x['link']
		desc = x['description']
		o =  {'title': z ,'description': desc}
		self.d[z] = o
	
		
	return d

class GetCache:
	def __init__(self,feedlink,age=0):
		cache_dir = app_home+"cache/"+get_md5(feedlink)
		body_cache = cache_dir+'.body'
		def update_shelf(self,key):
			d = shelve.open(cache_dir)
			del d[key]
			d.update(fp(feedlink))
			d.sync()
		if not os.path.exists(app_home+"cache/"):
			os.makedirs(app_home+"cache/")
		d = shelve.open(cache_dir)
		if (os.path.exists(cache_dir) and get_diff(time.time(),d[cache_dir]['time']) ):
			d.close()
			update_shelf(feedlink)
		else:
			d = shelve.open(cache_dir)
			f = d[feedlink][		
			
			
		
			
		def cache_url(self):
			openurl = urllib2.urlopen(feedlink)
			out = open(cache_dir+'.body','w')
			out.write(openurl.read())
			out.close()
			return True
		
			
					
		
		if os.path.exists(cache_dir) and os.path.exists(body_cache) :
			d = shelve.open(cache_dir)
			#f = open(cache_dir+'.body')
		if get_diff(time.time(), d[cache_dir]['time']):
			d[cache_dir] = {'time': time.time(),
			'url': feedlink}
			
			cache_url()
			
			
		
			
			
			
			
		else:
			
			
			
			get_url = urllib2.urlopen(feedlink)
			d  = shelve.open(cache_dir)
			d[cache_dir] = {'time': time.time(),
			'url': feedlink}
			
			f  = open(cache_dir+'.body', 'w')
			f.write(urllib2.urlopen(feedlink).read())
			d.close()
			f.close()
			d = shelve.open(cache_dir)
		
		
		
		self.li = d[cache_dir]['url']
		self.ti = d[cache_dir]['time']


class Cached_Object:
	def __init___(self,f):
		
		d = shelve.open(f,'r')
		self.links = d.items()
	
		selr.link = d[f]['url']		
		
		
