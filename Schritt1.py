# -*- coding: utf-8 -*-
"""
@author: aeb1
"""
from Schritte import BasisSchritt as b
from Schritte import Schritt2 as s

class Schritt1(b.BasisSchritt):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.lampen["LEFT_LOWER"].setZustand(False)
        self.components.lampen["RIGHT_LOWER"].setZustand(False)
        self.components.lampen["LEFT_UPPER"].setZustand(True)
        self.components.lampen["RIGHT_UPPER"].setZustand(True)
        self.components.ventile["LEFT_UPPER"].setZustand(True)
        self.components.ventile["RIGHT_UPPER"].setZustand(True)
        self.components.ventile["MIDDLE"].setZustand(True)
        self.components.ventile["LEFT_LOWER"].setZustand(False)
        self.components.ventile["RIGHT_LOWER"].setZustand(False)
        self.components.pumpe.setZustand(True)
        super().entry()

    def exit(self):
        self.components.lampen["LEFT_UPPER"].setZustand(False)
        self.components.lampen["RIGHT_UPPER"].setZustand(False)
        self.components.pumpe.setZustand(False)
        super().exit()
        
    def onSensor(self, sensorEvent):
        if str(sensorEvent).strip() == "sensor_right_middle wet":
            self.components.getAktuellerZustand().exit()
            self.components.setAktuellerZustand(s.Schritt2(self.components))
            #hier kommen alle Actions des Zustandsübergangs hin, falls vorhanden 
            self.components.getAktuellerZustand().entry()
        if str(sensorEvent).strip() == "sensor_bottom_lower dry":
            self.components.pumpe.setZustand(False)
        super().onSensor(sensorEvent)

    def onTimer(self):
        super().onTimer()
        