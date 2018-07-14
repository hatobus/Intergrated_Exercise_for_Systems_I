import tkinter as tk
from PIL import Image, ImageTk


def displayPhoto(event):
    im = Image.open("./downloadpic.png")
    photo = ImageTk.PhotoImage(im)
    cv.create_image(10, 10, image=photo, anchor='nw')
    root.mainloop()

root = tk.Tk()
root.title("Smart Photo Frame") 
root.geometry("1000x800")

Button = tk.Button(text="change picture", width = 50)
Button.bind("<Button-1>", displayPhoto)
Button.pack()

cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
root.mainloop()
