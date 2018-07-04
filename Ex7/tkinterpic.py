import tkinter as Tk
from PIL import Image, ImageTk


def printpush(event):
    im = PhotoImage(file = "./downloadpic.png")
    canvas.create_image(100, 100, image = im)
    canvas.pack()

root = Tk.Tk()
root.title("Smart PhotoFrame")
root.geometry("1000x800")

#ボタン
Button = Tk.Button(text="change picture", width=50)
Button.bind("<Button-1>", printpush)
Button.pack()

root.mainloop()
