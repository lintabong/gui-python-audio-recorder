import os
import tkinter
import threading
import sounddevice

from helper import config
from helper import fileManager

configuration = config.read()
h   = configuration["height"]
w   = configuration["width"]
cfh = configuration["controll"]["height"]

class MainFrame(tkinter.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.config(width=w, height=h-cfh, background="#B7BDDE")
        self.place(x=0, y=0)

        self.activeDir = ""

        self.fileFrame()

    def fileFrame(self):
        listframe = tkinter.Frame(self, width=w-40, height=h-(cfh+65), background="#B7BDDE")
        listframe.place(x=20, y=45)
        
        self.listDirectories = tkinter.Listbox(
            listframe, 
            height=8, 
            width=25,
            selectmode=tkinter.SINGLE)
        
        self.listFiles = tkinter.Listbox(
            listframe, 
            height=8, 
            width=25,
            selectmode=tkinter.SINGLE)
        
        tkinter.Button(
            listframe,
            text=">>",
            width=10, 
            height=2,
            command=self.openFolder).place(x=235, y=12)
        
        tkinter.Button(
            listframe,
            text="Play",
            width=10, 
            height=2,
            command=self.pathSound).place(x=235, y=100)

        self.listDirectories.place(x=0, y=0)
        self.listFiles.place(x=355, y=0)

        self.listDirectories.delete(0, tkinter.END)
        self.listFiles.delete(0, tkinter.END)

        for i, dir in enumerate(os.listdir("./result")):
            self.listDirectories.insert(i, dir)

    def pathSound(self):
        for i in self.listFiles.curselection():
            select = self.listFiles.get(i)

        self.filepath = fileManager.getSound(f'result/{self.activeDir}/{select}')

        threading.Thread(target=self.playSound).start()

    def playSound(self):
        sounddevice.play(self.filepath, 44100, device=3)
        sounddevice.wait()

    def openFolder(self):
        for i in self.listDirectories.curselection():
            self.activeDir = self.listDirectories.get(i)

        self.listFiles.delete(0, tkinter.END)

        for i, file in enumerate(os.listdir(f'./result/{self.activeDir}')):
            self.listFiles.insert(i, file)


class HomeFrame(tkinter.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.config(width=w, height=h-cfh, background="#219ebc")
        self.place(x=0, y=cfh)

        MainFrame(self)