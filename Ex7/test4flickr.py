import os
import settings
import shutil
import requests
from flickrapi import FlickrAPI
import random


FLICKRKEY = os.getenv("FLICKRKEY")
FLICKRSECRET = os.getenv("FLICKRSECRET")
MYID = os.getenv("MYUSERID")


def downloadPicture(url, filename):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

pageNum = 50

flickr = FlickrAPI(FLICKRKEY.encode('utf-8'), FLICKRSECRET, format='parsed-json')
photos = flickr.photos_search(user_id=MYID, per_page=pageNum)

print(photos)

# download picture 
# URL is this
# https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg

urllist = []

for i in range(pageNum):
    photoData = photos['photos']['photo'][i]

    farmId = photoData['farm']
    severId = photoData['server']
    picId = photoData['id']
    idSecreat = photoData['secret']
    
    url = "https://farm{0}.staticflickr.com/{1}/{2}_{3}.jpg".format(farmId, severId, picId, idSecreat)
    
    urllist.append(url)

dlURL = random.choice(urllist)

print(dlURL)

downloadPicture(dlURL, "downloadpic.jpg")
