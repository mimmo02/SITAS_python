from Komponenten import Pumpe as p
from Komponenten import Ventil as v
from Komponenten import Lampe as l
import threading as t
import socket
import time
import winsound

import Config as c
#connection configuration

host = c.host
commandProxy = 2008
eventProxy = 2009

class TankSystemProxy:  
    def __init__(self):
       self.host = host
       self.eventReader = None
       self.commandSocket = socket.socket()
       self.commandSocket.connect((host, commandProxy))
       self.eventSocket = socket.socket()
       self.eventSocket.connect((host, eventProxy))
       self.components = None
       self.timer = None

    def setComponents(self, components):
       self.components = components
       
    def forward(self, obj, zustand):
       if isinstance(obj, p.Pumpe):
          if (zustand):
             self.startPump()
          else:
             self.stopPump()
       elif isinstance(obj, v.Ventil):
          if (zustand):
             self.openValve(obj.getPosition())
          else:
             self.closeValve(obj.getPosition())
       elif isinstance(obj, l.Lampe):
          if (zustand):
             self.turnLampOn(obj.getPosition())
          else:
             self.turnLampOff(obj.getPosition())
            
    def reset(self):
        self.sendCommand("reset")
            
    def startPump(self):
        self.sendCommand("set pump on")

    def stopPump(self):
        self.sendCommand("set pump off")

    def openValve(self, position):
        if (position == "MIDDLE"):
            request = "set valve_bottom_lower on";
        else:
            request = "set valve_" + position + " on";
        self.sendCommand(request)
        
    def closeValve(self, position):
        if (position == "MIDDLE"):
            request = "set valve_bottom_lower off";
        else:
            request = "set valve_" + position + " off";
        self.sendCommand(request)
        
    def turnLampOn(self, position):
        self.sendCommand("set lamp_" + position + " on");

    def turnLampOff(self, position):
        self.sendCommand("set lamp_" + position + " off");

    def sendCommand(self, request):
        data = (request.lower() +"\n").encode()
        self.commandSocket.send(data)
            
    def notifyEvent(self, message):
        if message.startswith("reset"):
            self.onReset()
        elif message.startswith("ready"):
            self.onReady()
        elif message.startswith("sensor"):
            events = message.split(' ')
            tokens = events[0].split('_')
            name = "sensor_" + tokens[1]
            if(tokens[2] == "empty"):    
                name = name + "_lower"
            elif(tokens[2] == "half"):
                name = name + "_middle"
            elif(tokens[2] == "full"):
                name = name + "_upper"
            if  events[1].startswith("on"):
                name = name +" wet"
            elif events[1].startswith("off"):
                name = name +" dry"
            self.onSensor(name)
            
    def readEvents(self):
        while True:
            data = self.eventSocket.recv(1024).decode()
            if(data.strip() == "reset"):
                break
            self.notifyEvent(data)
            time.sleep(0.5)
        self.eventSocket.close()

    def onReset(self):
        winsound.Beep(1000, 500)

    def onReady(self):
        winsound.Beep(1000, 500)

    def onStart(self):
        t1 = t.Thread(target=self.readEvents, daemon=True)
        t1.start()
        #hier kommen die Befehle, welche vor dem Schritt 1 nötig sind.
        self.components.getAktuellerZustand().entry()

    def onTimer(self):
        self.components.getAktuellerZustand().onTimer();

    def onSensor(self, sensorEvent):
        self.components.getAktuellerZustand().onSensor(sensorEvent)

    def startTimer(self, n):
        self.timer = t.Timer(n, self.onTimer)
        self.timer.start()
        # wartet n Sekunden, bevor "onTimer" ausgeführt wird.
        
    def closeConnection(self):
        self.commandSocket.close()