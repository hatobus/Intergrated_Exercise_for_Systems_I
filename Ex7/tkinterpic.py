import tkinter as tk
from PIL import Image, ImageTk
import random


def displayPhoto(event):
    cv.delete("all")
    pic = ["./color_bar.png", "./lena.png", "./downloadpic.png"]
    im = Image.open(random.choice(pic))
    photo = ImageTk.PhotoImage(im)
    cv.create_image(10, 10, image=photo, anchor='nw')
    root.mainloop()

def takePhoto(event):
    print("hoge")

root = tk.Tk()
root.title("Smart Photo Frame") 
root.geometry("1000x800")

Buttonchange = tk.Button(text="change picture", width=50)
Buttontake = tk.Button(text="take picture", width=50)

Buttonchange.bind("<Button-1>", displayPhoto)
Buttontake.bind("<Button-2>", takePhoto)

Buttonchange.pack()
Buttontake.pack()

cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')

root.mainloop()
