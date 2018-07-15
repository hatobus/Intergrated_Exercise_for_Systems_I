import os
import settings
import shutil
import requests
from flickrapi import FlickrAPI
import random
import subprocess
import json
import lcd1602


FLICKRKEY = os.getenv("FLICKRKEY")
FLICKRSECRET = os.getenv("FLICKRSECRET")
MYID = os.getenv("MYUSERID")

class iesPicture():
    def __init__(self, pageNum=50):

        self.flickr = FlickrAPI(FLICKRKEY.encode('utf-8'),
                                FLICKRSECRET,
                                format='parsed-json'
                                )

        if not self.flickr.token_valid():
            self.flickr.get_request_token(oauth_callback="oob")

            verifier = str(input(
                "Get verifier code from {} and enter it here.\n: "
                .format(self.flickr.auth_url(perms="write"))))

            self.flickr.get_access_token(verifier)

        self.LCD = lcd1602.LCD16021()

    def choosePrintPicture(self, pageNum=50):
        photos = self.flickr.photos_search(
            user_id=MYID,
            per_page=pageNum
        )

        urltitledict = {}

        for i in range(pageNum):
            photoData = photos['photos']['photo'][i]

            farmId = photoData['farm']
            severId = photoData['server']
            picId = photoData['id']
            idSecreat = photoData['secret']
            title = photoData["title"]

            url = "https://farm{0}.staticflickr.com/{1}/{2}_{3}.jpg".format(farmId, severId, picId, idSecreat)

            urltitledict[url] = title

        dlURL, title = random.choice(list(urltitledict.items()))

        print(dlURL)

        self.LCD.lcd_string("Title", 0x80)
        self.LCD.lcd_string(title, 0xC0)

        self.downloadPicture(dlURL, "./Image/downloadpic.jpg")
        self.pictureConvert("./Image/downloadpic.jpg")

    def downloadPicture(self, url, filename):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

    def pictureConvert(self, name):
        root, ext = os.path.splitext(name)
        newext = ".png"
        args = ['convert', name, root+newext]
        res = subprocess.check_call(args)
        print(res)

    def uploadPhoto(self, path_to_photo, title=None):

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
        """
        if not api.token_valid():
            api.get_request_token(oauth_callback="oob")

            verifier = str(input("Get verifier code from {} and enter it here.\n: ".format(api.auth_url(perms="write"))))

            api.get_access_token(verifier)
        """

        try:
            res = self.flickr.upload(
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


if __name__ == '__main__':
    ies = iesPicture()
    ies.choosePrintPicture()
    ies.uploadPhoto("./testpicture.png")
