# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

import tkinter as tk
import tkinter.font as tkFont
from View.PlaceButtons import placeButtons
import View.MainControl as mc


from Utils import TankSystemProxy as t     
from Utils import Initialization as i     

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
     
#create root window
root = tk.Tk()
def_font = tkFont.nametofont("TkDefaultFont")
def_font.config(size=12)

width=500
height=500
xpos = 150
ypos = 150
root.geometry(f'{width}x{height}+{xpos}+{ypos}')

#set window title
root.title('SiTas MainWindow')
mainControl = mc.MainControl()


#init some busines classes
tankSystemProxy = t.TankSystemProxy()            
components = i.Initialization(tankSystemProxy)    

mainControl.setTanksystemProxy(tankSystemProxy)    
mainControl.setComponents(components)        
tankSystemProxy.setComponents(components)    


placeButtons(root, mainControl)

# keep the window displaying
root.mainloop()


