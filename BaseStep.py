# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

import Config as c
fileName = c.logFileName

class BaseStep:
    def __init__(self, components):
        self.components = components
    
    def entry(self):
        self.writeLog(str(self) + " entry")

    def exit(self):
        self.writeLog(str(self) + " exit")

    def onSensor(self, sensorEvent):
        text = str(self) + " onSensor: "+str(sensorEvent)
        self.writeLog(text)  

    def onTimer(self):
        self.writeLog(str(self) + " onTimer")
        
    def writeLog(self, text):
        with open(fileName, 'a') as file:
            file.write(text + "\n")  
    
    def __str__(self):
        return str(self.components.repetition) +": "+ str(type(self).__name__)