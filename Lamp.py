# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:43:02 2024

@author: Aquil
"""

from Components import TankComponent as t

class Lamp(t.TankComponent):
    def __init__(self,proxy,position):
        super().__init__(proxy)
        self.__position = position
        
    def getPosition(self):
        return self.__position
    
    def setPosition(self,position):
        self.__position = position
        
    def setState(self,state):
        super().setState(state)
        super().getProxy().forward(self,state)
        