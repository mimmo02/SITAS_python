# -*- coding: utf-8 -*-
"""
@author: aeb1
"""
from Components import Pump as p
from Components import Lamp as l
from Components import Valve as v
from Steps import Step0 as s
     
class Initialization:
    def __init__(self, proxy):
        self.proxy = proxy
        self.valves = self.createValves()
        self.lamps = self.createLamps()
        self.pump = self.createPump()
        self.repetition = 1
        self.currentStep = s.Step0(self)
     
    def createValves(self):
        valves = dict()
        valves["LEFT_LOWER"] = v.Valve("LEFT_LOWER", self.proxy)
        valves["LEFT_UPPER"] = v.Valve("LEFT_UPPER", self.proxy)
        valves["RIGHT_LOWER"] = v.Valve("RIGHT_LOWER", self.proxy)
        valves["RIGHT_UPPER"] = v.Valve("RIGHT_UPPER", self.proxy)
        valves["MIDDLE"] = v.Valve("MIDDLE", self.proxy)
        return valves
        
    def createLamps(self):
        lamps = dict()
        lamps["LEFT_LOWER"] = l.Lamp("LEFT_LOWER", self.proxy)
        lamps["LEFT_UPPER"] = l.Lamp("LEFT_UPPER",  self.proxy)
        lamps["RIGHT_LOWER"] = l.Lamp("RIGHT_LOWER",  self.proxy)
        lamps["RIGHT_UPPER"] = l.Lamp("RIGHT_UPPER",  self.proxy)
        return lamps    
    
    def createPump(self):
        return p.Pump(self.proxy)
    
    def getValve(self,position):
        return self.valves[position]

    def getLamp(self,position):
        return self.lamps[position] 
    
    def getPump(self):
        return self.pump
    
    def getCurrentStep(self):
        return self.currentStep
    
    def setCurrentStep(self, step):
        self.currentStep = step
    
    def getRepetition(self):
        return self.repetition
    
    def nextRepetition(self):
        self.repetition = self.repetition + 1
    
    def startTimer(self, n):
        self.proxy.startTimer(n)
        
