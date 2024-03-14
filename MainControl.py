# -*- coding: utf-8 -*-
"""
@author: aeb1
"""
     
class MainControl:
    def __init__(self) -> None:
        self.proxy = None
        self.components = None
    
    def setTanksystemProxy(self, tanksystemProxy):
        self.proxy = tanksystemProxy
        
    def setComponents(self, components):
        self.components = components

    def setPumpeZustand(self, zustand) -> None:
        if zustand == 0:
            self.__setPumpeZustand(False)
        else:
            self.__setPumpeZustand(True)
        
    def __setPumpeZustand(self, zustand) -> None:
        self.components.getPumpe().setZustand(zustand)

    def setVentilZustand(self, position, zustand) -> None:
        if zustand.get() == 0:
            self.__setVentilZustand(position, False)
        else:
            self.__setVentilZustand(position, True)

    def __setVentilZustand(self, position, zustand) -> None:
            self.components.getVentil(position).setZustand(zustand)  

    def setLampeZustand(self, position, zustand) -> None:
        if zustand.get() == 0:
           self.__setLampeZustand(position, False)
        else:
            self.__setLampeZustand(position, True)
 
    def __setLampeZustand(self,position, zustand) -> None:
             self.components.getLampe(position).setZustand(zustand)  

    def reset(self) -> None:
        self.proxy.reset()

    def start(self) -> None:
        self.proxy.onStart()

    def exit(self, root) -> None:
        self.setPumpeZustand(0)
        root.destroy()
        self.proxy.closeConnection()
