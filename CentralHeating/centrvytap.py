import time

class CentralHeating:

    def __init__(self, name, begin_temp, start_heating, stop_heating):
        self.name = name
        self.begin_temp = begin_temp
        self.start_heating = start_heating
        self.stop_heating = stop_heating

    self.heating = True
    self.actual_temp = begin_temp
    self.begin_time = time.time()
    print(f"Topení {self.name} je ZAPNUTO a má {self.actual_temp} °C")

@staticmethod
def boolToSwitch(toSwitch):
    if toSwitch:
        return "ZAPNUTO"
    else:
        return "VYPNUTO"
    
@classmethod
def setOutsideTemperature(cls, temperature):
    cls.outsideTemperature = temperature

@classmethod
def startCentralHeating(cls):
    cls.centralHeating = True
    
@classmethod
def startCentralHeating(cls):
    cls.centralHeating = False

def regulateHeating(self):
    myTime = self.begin_time - time.time()
    if self.heating:
        self.actual_temp = self.begin_temp
CentralHeating.setOutsideTemperature(12)
CentralHeating.startCentralHeating()

heating1 = CentralHeating("obývák", 0.7, 16, 19, 23)

