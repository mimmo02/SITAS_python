# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

import tkinter as tk
import tkinter.font as tkFont
from View.PlaceButtons import placeButtons
import View.MainControl as mc

# from Utils import TankSystemProxy as t     // remove comment here  !!!!
#from Utils import Initialisierung as i      // remove comment here  !!!!
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
     
#create root window
root = tk.Tk()
def_font = tkFont.nametofont("TkDefaultFont")
def_font.config(size=12)

width=700
height=650
xpos = 150
ypos = 150
root.geometry(f'{width}x{height}+{xpos}+{ypos}')

#set window title
root.title('SiTas MainWindow')

#init some busines classes
#tankSystemProxy = t.TankSystemProxy()            // remove comment here  !!!!

#components = i.Initialisierung(tankSystemProxy)    // remove comment here  !!!!
mainControl = mc.MainControl()
#mainControl.setTankSystemProxy(tankSystemProxy)    // remove comment here  !!!!
#mainControl.setComponents(components)         // remove comment here  !!!!
#tankSystemProxy.setComponents(components)    // remove comment here  !!!!

placeButtons(root, mainControl)

# keep the window displaying
root.mainloop()


