# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

from Schritte import BasisSchritt as b
from Schritte import Schritt1 as s

class Schritt3(b.BasisSchritt):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.lampen["LEFT_LOWER"].setZustand(False)  
        self.components.lampen["RIGHT_LOWER"].setZustand(False)
        super().entry()

    def exit(self):
        super().exit()

    def onSensor(self, sensorEvent):
        if str(sensorEvent).strip() == "sensor_left_lower dry":
            self.components.nextDurchlauf()
            if self.components.durchlauf <= 2:
                self.components.getAktuellerZustand().exit()
                self.components.setAktuellerZustand(s.Schritt1(self.components))
                #Hier sind alle Aktionen des Übergangs
                self.components.pumpe.setZustand(True)
                self.components.getAktuellerZustand().entry()
        super().onSensor(sensorEvent)

    def onTimer(self):
        super().onTimer()        
        
        