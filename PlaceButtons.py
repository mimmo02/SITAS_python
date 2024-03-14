# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:48:59 2022
@author: aeb1
"""
import tkinter as tk
from tkinter import ttk

bWidth = 18
   
# place some buttons on the root window
def placeButtons(root, mainControl) -> None:
    VOLstate = tk.IntVar()
    VORstate = tk.IntVar()
    VULstate = tk.IntVar()
    VURstate = tk.IntVar()
    VMstate = tk.IntVar()
    
    LOLstate = tk.IntVar()
    LORstate = tk.IntVar()
    LULstate = tk.IntVar()
    LURstate = tk.IntVar()
 
    sep = ttk.Separator(root,orient='horizontal')
    sep.grid(row=0, column=0, columnspan=2, pady=10)
    
    labelV = ttk.Label(root, font=("Arial", 16))
    labelV['text'] = 'Ventile'
    labelV.grid(row=1, column=0, columnspan = 2, padx=5, pady=5)
    
    vOL = ttk.Checkbutton(root, text="oben links", variable=VOLstate,
            command=lambda:mainControl.setVentilZustand("LEFT_UPPER", VOLstate))
    vOL.grid(row=2,column=0, padx=25, pady=5)

    vOR = ttk.Checkbutton(root, text="oben rechts", variable=VORstate,
            command=lambda:mainControl.setVentilZustand("RIGHT_UPPER", VORstate))
    vOR.grid(row=2,column=1, padx=25, pady=5)

    vUL = ttk.Checkbutton(root, text="unten links", variable=VULstate,
            command=lambda:mainControl.setVentilZustand("LEFT_LOWER", VULstate))
    vUL.grid(row=3,column=0, padx=25, pady=5)

    vUR = ttk.Checkbutton(root, text="unten rechts", variable=VURstate,
            command=lambda:mainControl.setVentilZustand("RIGHT_LOWER", VURstate))
    vUR.grid(row=3,column=1, padx=25, pady=5)

    vM = ttk.Checkbutton(root, text="mitte", variable=VMstate, 
          command=lambda:mainControl.setVentilZustand("MIDDLE", VMstate))
    vM.grid(row=4,column=0, columnspan=2)
    
    sep = ttk.Separator(root,orient='horizontal')
    sep.grid(row=5, column=0, columnspan=2, pady=10)
    
    labelL = ttk.Label(root, font=("Arial", 16))
    labelL['text'] = 'Lampen'
    labelL.grid(row=6, column=0, columnspan = 2, padx=5, pady=5)
    
    
    lOL = ttk.Checkbutton(root, text="oben links", variable=LOLstate,
        command=lambda:mainControl.setLampeZustand("LEFT_UPPER", LOLstate))
    lOL.grid(row=7,column=0, padx=15, pady=5)
    
    
    lOR = ttk.Checkbutton(root, text="oben rechts", variable=LORstate,
        command=lambda:mainControl.setLampeZustand("RIGHT_UPPER", LORstate))
    lOR.grid(row=7,column=1, padx=15, pady=5)
    
    
    lUL = ttk.Checkbutton(root, text="unten links", variable=LULstate,
        command=lambda:mainControl.setLampeZustand("LEFT_LOWER", LULstate))
    lUL.grid(row=8,column=0, padx=15, pady=5)
    
    
    lUR = ttk.Checkbutton(root, text="unten rechts", variable=LURstate,
        command=lambda:mainControl.setLampeZustand("RIGHT_LOWER", LURstate))
    lUR.grid(row=8,column=1, padx=15, pady=5)
    
    sep = ttk.Separator(root,orient='horizontal')
    sep.grid(row=9, column=0, columnspan=2, padx=15, pady=15)
    
    pumpe_ein = ttk.Button(root, text="Pumpe ein", width=bWidth,
            command=lambda:mainControl.setPumpeZustand(1))
    pumpe_ein.grid(row=10,column=0, padx=15, pady=15)
    
    pumpe_aus = ttk.Button(root, text="Pumpe aus", width=bWidth,
        command=lambda:mainControl.setPumpeZustand(0))
    pumpe_aus.grid(row=10,column=1, padx=15, pady=15)

    # start button
    ttk.Button(root,
        text=' Start ', width=bWidth,
        command=lambda: mainControl.start()
        ).grid(row=11, column=0, padx=15, pady=5)

    # exit button
    ttk.Button(root,
        text=' Exit ', width=bWidth,
        command=lambda: mainControl.exit(root)
        ).grid(row=11, column=1, padx=15, pady=5)

