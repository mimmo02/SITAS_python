# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:15:23 2024

@author: fabio
"""

from Steps import BaseStep as b
from Steps import Step1 as s
from Steps import End as e

class Step7(b.BaseStep):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.pump.setState(False)
        self.components.lamps["LEFT_LOWER"].setState(False)
        self.components.lamps["RIGHT_LOWER"].setState(False)
        self.components.lamps["LEFT_UPPER"].setState(False)
        self.components.lamps["RIGHT_UPPER"].setState(False)
        self.components.valves["LEFT_UPPER"].setState(True)
        self.components.valves["RIGHT_UPPER"].setState(True)
        self.components.valves["MIDDLE"].setState(False)
        self.components.valves["LEFT_LOWER"].setState(True)
        self.components.valves["RIGHT_LOWER"].setState(True)
        super().entry()

    def exit(self):
        super().exit()
        
    def onSensor(self, sensorEvent):
        if str(sensorEvent).strip() == "sensor_right_lower dry":
            self.components.nextRepetition()
            if self.components.repetition <= 2:
                self.components.getCurrentStep().exit()
                self.components.setCurrentStep(s.Step1(self.components))
                self.components.getCurrentStep().entry()
            else:
                self.components.getCurrentStep().exit()
                self.components.setCurrentStep(e.End(self.components))
                self.components.getCurrentStep().entry()
        super().onSensor(sensorEvent)
        
    def onTimer(self):
        super().onTimer()
    
 