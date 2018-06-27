import os
import requests
from flickrapi import FlickrAPI
import takepic
import time, datetime


FLICKRKEY = os.getenv("FLICKRKEY")
FLICKRSECRET = os.getenv("FLICKRSECRET")
MYID = os.getenv("MYUSERID")


PIC = takepic.takePic()
PIC.takePic()
UPLOADPICPATH = "./tookpic/uploadpic.jpg"

#flickr = FlickrAPI(FLICKRKEY, FLICKRSECRET, format='parsed-json')

now = datetime.datetime.now()
nowHMS = str(now.hour) + str(now.minute) + str(now.second)

upFileTitle = "IEStest" + nowHMS

#flickr.upload(UPLOADPICPATH, upFileTitle)

params = {
    'photo'          : UPLOADPICPATH,
    'title'          : upFileTitle,
}

r = requests.post('https://up.flickr.com/services/upload/', params=params)
print(r.content)
