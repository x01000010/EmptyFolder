__author__ = 'x01000010'

from tkinter import *
from tkinter import filedialog
import os


def run_button():
    print("workning")
    for dirpath, dirnames, files in os.walk(e1.get()):
        if not files and not dirnames:
            print(dirpath)
            os.rmdir(dirpath)

    print("done")


def callback():
    name = filedialog.askdirectory()
    e1.insert(0, name)

master = Tk()
msg = Message(master,text="")
msg.grid(row=1)
Label(master, text="Start Folder").grid(row=0)
e1 = Entry(master)

e1.grid(row=0, column=1)
Button(master, text="Browse", command=callback).grid(row=0, column=2)
Button(master, text="run", command=run_button).grid(row=2)
Button(master, text="quit", command=master.quit).grid(row=2, column=1)

mainloop()
