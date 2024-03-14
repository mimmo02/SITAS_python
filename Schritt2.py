# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

from Schritte import BasisSchritt as b
from Schritte import Schritt3 as s

class Schritt2(b.BasisSchritt):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.startTimer(4)
        self.components.lampen["LEFT_LOWER"].setZustand(True)
        self.components.lampen["RIGHT_LOWER"].setZustand(True)
        self.components.ventile["LEFT_LOWER"].setZustand(True)
        self.components.ventile["RIGHT_LOWER"].setZustand(True)
        self.components.ventile["MIDDLE"].setZustand(True)
        super().entry()

    def exit(self):
        self.components.lampen["RIGHT_LOWER"].setZustand(False)
        self.components.lampen["LEFT_LOWER"].setZustand(False)  
        super().exit()

    def onSensor(self, sensorEvent):
        super().onSensor(sensorEvent)

    def onTimer(self):
        self.components.getAktuellerZustand().exit()
        self.components.setAktuellerZustand(s.Schritt3(self.components))
        #Hier sind alle Aktionen des Übergangs
        self.components.getAktuellerZustand().entry()
        super().onTimer()        
        
        