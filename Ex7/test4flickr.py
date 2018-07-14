import os
import settings
import shutil
import requests
from flickrapi import FlickrAPI
import random
import subprocess
import Upload
import json


FLICKRKEY = os.getenv("FLICKRKEY")
FLICKRSECRET = os.getenv("FLICKRSECRET")
MYID = os.getenv("MYUSERID")


def upload_photo(api, path_to_photo, title=None):
    """ Upload the photo file to flickr.
    arguments:
        api: FlickrAPI object.
        path_to_photo: Path to photo file.
        title: photo file's name if None.
    returns:
        uploaded photo ID if success, else None.
    """
    # res is instance of xml.etree.ElementTree.Element.
    # This element has something like "<rsp><photoid>1234</photoid></rsp>".
    if not api.token_valid():
        api.get_request_token(oauth_callback="oob")

        verifier = str(input("Get verifier code from {} and enter it here.\n: ".format(api.auth_url(perms="write"))))

        api.get_access_token(verifier)

    try:
        res = api.upload(
            filename=path_to_photo,
            title=os.path.basename(path_to_photo) if not title else title,
            is_private=True
            )

    except json.decoder.JSONDecodeError:
        return None

    if res.get("stat") != "ok":
        return None

    # Get the uploaded photo's ID.
    return res


def downloadPicture(url, filename):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def pictureConvert(name):
    root, ext = os.path.splitext(name)
    newext = ".png"
    args = ['convert', name, root+newext]
    res = subprocess.check_call(args)
    print(res)


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
pictureConvert("downloadpic.jpg")

rest = upload_photo(flickr, "./testpicture.png", title="Test")
