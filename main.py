import feedparser
import argparse
import os
import json
import hashlib
import time
import urllib2
import urllib2
import cherrypy
from newsreader.Cache import GetCache
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))



app_home = os.path.expanduser("~")+'/.newsreader/'
cache_dir = os.getcwd()+'.cache'
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




class Root(object):
    @cherrypy.expose
    def index(self):
        shit = 'This is where the main content goes'
        tmpl =  env.get_template('index.html')
        return tmpl.render(stuff=shit)




if __name__ == '__main__':
    cherrypy.config.update({'tools.staticdir.on': True,
                'tools.staticdir.dir': '/home/sean/projects/newsreader/newsreader'
               })
    cherrypy.quickstart(Root())













