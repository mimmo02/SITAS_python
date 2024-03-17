# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:07:36 2024

@author: Aquil
"""

from Components import TankComponent as t

class Valve(t.TankComponent):
    
    def __init__(self,position,proxy):
        super().__init__(proxy)
        self.__position = position
        
    def getPosition(self):
        return self.__position
    
    def setPosition(self,position):
        self.__position = position
        
    def setState(self,state):
        super().setState(self,state)
        super().getProxy().forward(self,state)
        