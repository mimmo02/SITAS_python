# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:11:52 2024

@author: Aquil
"""

from Components import TankComponent as t

class Sensor(t.TankComponent):
    
    def __init__(self,proxy,position):
        super().__int__(proxy)
        self.__position = position
        
    def getPosition(self):
        return self.__position
    
    def setPosition(self,position):
        self.__position = position
        
        
    def getState(self):
        return super().getState()