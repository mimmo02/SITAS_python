# -*- coding: utf-8 -*-
"""
@author: aeb1
"""
from Komponenten import Pumpe as p
from Komponenten import Lampe as l
from Komponenten import Ventil as v
from Schritte import Schritt1
     
class Initialisierung:
    def __init__(self, proxy):
        self.proxy = proxy
        self.ventile = self.createVentile()
        self.lampen = self.createLampen()
        self.pumpe = self.createPumpe()
        self.durchlauf = 1
        self.aktuellerZustand = Schritt1.Schritt1(self)
     
    def createVentile(self):
        ventile = dict()
        ventile["LEFT_LOWER"] = v.Ventil("LEFT_LOWER", self.proxy)
        ventile["LEFT_UPPER"] = v.Ventil("LEFT_UPPER", self.proxy)
        ventile["RIGHT_LOWER"] = v.Ventil("RIGHT_LOWER", self.proxy)
        ventile["RIGHT_UPPER"] = v.Ventil("RIGHT_UPPER", self.proxy)
        ventile["MIDDLE"] = v.Ventil("MIDDLE", self.proxy)
        return ventile
        
    def createLampen(self):
        lampen = dict()
        lampen["LEFT_LOWER"] = l.Lampe("LEFT_LOWER", self.proxy)
        lampen["LEFT_UPPER"] = l.Lampe("LEFT_UPPER",  self.proxy)
        lampen["RIGHT_LOWER"] = l.Lampe("RIGHT_LOWER",  self.proxy)
        lampen["RIGHT_UPPER"] = l.Lampe("RIGHT_UPPER",  self.proxy)
        return lampen    
    
    def createPumpe(self):
        return p.Pumpe(self.proxy)
    
    def getVentil(self,position):
        return self.ventile[position]

    def getLampe(self,position):
        return self.lampen[position] 
    
    def getPumpe(self):
        return self.pumpe
    
    def getAktuellerZustand(self):
        return self.aktuellerZustand
    
    def setAktuellerZustand(self, zustand):
        self.aktuellerZustand = zustand
    
    def getDurchlauf(self):
        return self.durchlauf
    
    def nextDurchlauf(self):
        self.durchlauf = self.durchlauf + 1
    
    def startTimer(self, n):
        self.proxy.startTimer(n)
        
