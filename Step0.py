# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:52:48 2024

@author: fabio
"""


from Steps import BaseStep as b
from Steps import Step1 as s

class Step0(b.BaseStep):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.startTimer(18)
        self.components.lamps["LEFT_LOWER"].setState(False)
        self.components.lamps["RIGHT_LOWER"].setState(False)
        self.components.lamps["LEFT_UPPER"].setState(False)
        self.components.lamps["RIGHT_UPPER"].setState(False)
        self.components.valves["LEFT_UPPER"].setState(True)
        self.components.valves["RIGHT_UPPER"].setState(True)
        self.components.valves["MIDDLE"].setState(True)
        self.components.valves["LEFT_LOWER"].setState(True)
        self.components.valves["RIGHT_LOWER"].setState(True)
        self.components.pump.setState(False)
        super().entry()

    def exit(self):
        super().exit()
        
    def onSensor(self, sensorEvent):
        super().onSensor(sensorEvent)
        
    def onTimer(self):
        self.components.getCurrentStep().exit()
        self.components.setCurrentStep(s.Step1(self.components))
        
        self.components.getCurrentStep().entry()
        super().onTimer()
    
 