import tkinter as tk
from PIL import Image, ImageTk
import IESpicture
import subprocess
import re
import webcam


def displayPhoto(event):
    cv.delete("all")
    ies.choosePrintPicture()
    cmd = "identify -format '%wx%h\\n' ./Image/downloadpic.png"

    ret = subprocess.Popen(cmd.split(),
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=False
                           )

    size_byte = ret.stdout.readlines()[0]
    size_utf_8 = size_byte.decode("UTF-8")
    size_re = re.sub('\'|\\n', '', size_utf_8)
    size_x, size_y = size_re.split("x")

    scale_w = int(900/int(size_x))
    scale_h = int(700/int(size_y))

    im = Image.open("./Image/downloadpic.png")
    #im.resize((scale_w, scale_h), Image.ANTIALIAS)
    im = im.resize((900, 600), Image.LANCZOS)
    photo = ImageTk.PhotoImage(im)
    #photo.zoom(scale_w, scale_h)
    cv.create_image(500, 400, image=photo)
    root.mainloop()

def takePhoto(event):
    cam.takePic()
    uploadPictureFile = "./tookpic/uploadpic.jpg"

    ies.uploadPhoto(uploadPictureFile)


ies = IESpicture.iesPicture()
cam = webcam.takePic()

root = tk.Tk()
root.title("Smart Photo Frame")
root.geometry("1000x800")

Buttonchange = tk.Button(text="change picture", width=50)
Buttontake = tk.Button(text="take picture", width=50)

Buttonchange.bind("<Button-1>", displayPhoto)
Buttontake.bind("<Button-1>", takePhoto)

Buttonchange.pack()
Buttontake.pack()

cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')

root.mainloop()
