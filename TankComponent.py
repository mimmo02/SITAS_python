# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:37:29 2024

@author: Aquil
"""

class TankComponent:
    def __init__(self,proxy):
        self.__state = False
        self.__proxy = proxy
        
    def getState(self):
        return self.__state
    
    def setState(self,state):
        self.__state = state
    
    def getProxy(self):
        return self.__proxy
    
    
    
    