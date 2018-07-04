import tkinter as Tk
from PIL import Image, ImageTk


class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.pack()
        self.createCanvas()

    def printpush(self, event):
        print("Pushed")

    def createCanvas(self):
        root.title("Smart PhotoFrame")
        root.geometry("400x300")
        
        #ボタン
        Button = Tk.Button(text='ボタンです', width=50)
        Button.bind("<Button-1>", printpush)
        Button.pack()

        
root = Tk.Tk()
app = Application(master=root)
app.mainloop()
