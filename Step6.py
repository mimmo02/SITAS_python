# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:52:48 2024

@author: fabio
"""


from Steps import BaseStep as b
from Steps import Step7 as s

class Step6(b.BaseStep):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.pump.setState(True)
        self.components.lamps["LEFT_LOWER"].setState(False)
        self.components.lamps["RIGHT_LOWER"].setState(True)
        self.components.lamps["LEFT_UPPER"].setState(True)
        self.components.lamps["RIGHT_UPPER"].setState(False)
        self.components.valves["LEFT_UPPER"].setState(False)
        self.components.valves["RIGHT_UPPER"].setState(True)
        self.components.valves["MIDDLE"].setState(True)
        self.components.valves["LEFT_LOWER"].setState(True)
        self.components.valves["RIGHT_LOWER"].setState(False)
        super().entry()

    def exit(self):
        super().exit()
        
    def onSensor(self, sensorEvent):
        if str(sensorEvent).strip() == "sensor_right_middle wet":
            self.components.valves["RIGHT_UPPER"].setState(False)
            self.components.lamps["RIGHT_UPPER"].setState(True)
            self.components.pump.setState(False)
        if str(sensorEvent).strip() == "sensor_left_middle dry":
            self.components.getCurrentStep().exit()
            self.components.setCurrentStep(s.Step7(self.components))
            self.components.getCurrentStep().entry()
        super().onSensor(sensorEvent)
        
    def onTimer(self):
        super().onTimer()
    
 