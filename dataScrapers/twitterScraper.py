#!/users/Janan/anaconda/bin/python

import oauth2 as oauth
from elementtree.SimpleXMLWriter import XMLWriter
import json
import codecs

with open("apikey.txt") as f:
	for line in f:
		if line.startswith("TWITTER_CONSUMER_KEY"):
			CONSUMER_KEY = line.split("=")[1].strip()
		if line.startswith("TWITTER_CONSUMER_SECRET"):
			CONSUMER_SECRET = line.split("=")[1].strip()
		if line.startswith("TWITTER_ACCESS_KEY"):
			ACCESS_KEY = line.split("=")[1].strip()
		if line.startswith("TWITTER_ACCESS_SECRET"):
			ACCESS_SECRET = line.split("=")[1].strip()

def oauth_request(url, http_method="GET",post_body =None, http_headers=None):
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, access_token)
    resp, content = client.request(url,method=http_method)
    return content

def search():
    URL = 'https://api.twitter.com/1.1/search/tweets.json?'
    Count = '&count=100'
    DCGeocode='&geocode=38.895,-77.036389,4.5mi'
    URL = URL + Count + DCGeocode 
    return oauth_request(URL)

if __name__ == "__main__":
    f = codecs.open('test.xml', mode = 'w')
    w = XMLWriter(f)

    dictionary = json.loads(search())


    for n in range(0,len(dictionary["statuses"])):
        entry = dictionary["statuses"][n]
        if(not(entry["geo"] == None)):
            w.start('dataelement')
            w.element('text', "Status: " + entry["text"].encode('ascii','ignore') + '\n')
            w.start('geodata')
            w.element('lattitude',str(entry["geo"]["coordinates"][0]))
            w.element('longitude',str(entry["geo"]["coordinates"][1]))
            w.end('geodata')
            w.end('dataelement')

        
