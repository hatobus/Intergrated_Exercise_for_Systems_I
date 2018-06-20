import os
import time
import settings
import json
from flickrapi import FlickrAPI


FLICKRKEY = os.getenv("FLICKRKEY")
FLICKRSECRET = os.getenv("FLICKRSECRET")
MYID = os.getenv("MYUSERID")

waitTime = 10

flickr = FlickrAPI(FLICKRKEY, FLICKRSECRET, format='parsed-json')
photos = flickr.photos_search(user_id=MYID, per_page='1')

print(photos)

# download picture 
# URL is this
# https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg

photoData = photos['photos']['photo'][0]

farmId = photoData['farm']
severId = photoData['server']
picId = photoData['id']
idSecreat = photoData['secret']

url = "https://farm{0}.staticflickr.com/{1}/{2}_{3}.jpg".format(farmId, severId, picId, idSecreat)

print(farmId)
print(url)
