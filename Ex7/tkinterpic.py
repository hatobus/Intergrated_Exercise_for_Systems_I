import tkinter as Tk
from PIL import Image, ImageTk


def printpush(event):
    print("Pushed")

root = Tk.Tk()
root.title("Smart PhotoFrame")
root.geometry("400x300")

#ボタン
Button = Tk.Button(text="change picture", width=50)
Button.bind("<Button-1>", printpush)
Button.pack()

root.mainloop()
