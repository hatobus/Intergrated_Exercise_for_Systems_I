from tkinter import Tk, ttk, PhotoImage
from PIL import Image, ImageTk

root = Tk()

img = PhotoImage(file='../downloadpic.jpg')

label = ttk.Label(root, image=img)
label.grid()
