#CREATE THE CLASS
class Car(object):
    #CREATE THE CONSTRUCTOR __INIT__
    def __init__(self,model,color,company,speedLimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit
    
    #CREATE SOME FUNCTIONS
    def start(self):
        print("STARTED")
    

    def stop(self):
        print("STOP")

    def accelarate(self):
        print("ACCELARATING")

    def changeGear(self):
        print("GEAR CHANGED")

    

#CREATE OBJECTS & PRINT AND CALL THE FUNCTIONS
car1 = Car("ZK101","Black","TATA","200")
print(car1.start())
print(car1.stop())
print(car1.accelarate())
print(car1.changeGear())
