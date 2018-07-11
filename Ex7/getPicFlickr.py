import os
import settings
import shutil
import random
import subprocess
import requests

from flickrapi import FlickrAPI

FLICKRKEY = os.getenv("FLICKRKEY")
FLICKRSECRET = os.getenv("FLICKRSECRET")
MYID = os.getenv("MYUSERID")

class pictureGET():
    def _init__(self, fname="download.jpg"):
        self.pageNum = 100
        self.fname = fname

    def picDL(self, url, fname):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(fname, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

    def convertExt(self, fname):
        root, ext = os.path.splitext(fname)
        newext = ".png"
        args = ['convert', fname, root+newext]
        res = subprocess.check_call(args)
        print(res)

    def getpicture(self):
        flickr = FlickrAPI(FLICKRKEY.encode('utf-8'), FLICKRSECRET, format='parsed-json')
        photos = flickr.photos_search(user_id=MYID, per_page=100)

        urllist = []

        for i in range(100):
            photoData = photos['photos']['photo'][i]
            farmId = photoData['farm']
            severId = photoData['server']
            picId = photoData['id']
            idSecreat = photoData['secret']
     
        url = "https://farm{0}.staticflickr.com/{1}/{2}_{3}.jpg".format(farmId, severId, picId, idSecreat)
    
        urllist.append(url)
    
        dlURL = random.choice(urllist)

        self.picDL(dlURL, "downloadpic.jpg")

        self.convertExt("downloadpic.jpg")


if __name__ == "__main__":
    pic = pictureGET()
    pic.getpicture()

