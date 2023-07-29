import tkinter
import threading
import json
import time
import math
import copy
import re

from datetime import datetime

from helper import config

configuration = config.read()
h   = configuration["height"]
w   = configuration["width"]
cfh = configuration["controll"]["height"]

class MainFrame(tkinter.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.config(width=w, height=h-cfh, background="#B7BDDE")
        self.place(x=0, y=0)

    def SerialFrame(self):
        serrFrame = tkinter.LabelFrame(self, width=380, height=220, background="#B7BDDE", text="  Port Serial  ")
        serrFrame.place(x=20, y=20)

class HomeFrame(tkinter.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.config(width=w, height=h-cfh, background="#219ebc")
        self.place(x=0, y=cfh)

        MainFrame(self)