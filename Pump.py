# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:55:18 2024

@author: Aquil
"""

from Components import TankComponent as t

class Pump(t.TankComponent):
    
    def __init__(self, proxy):
        super().__init__(proxy)
        
    def setState(self,state):
        super().setState(state)
        super().getProxy().forward(self,state)
    