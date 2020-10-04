#CREATE THE CLASS
class Guitar(object):
    #CREATE __INIT__
    def __init__(self,guitarType,Company,Price):
        self.guitarType = guitarType
        self.Company = Company
        self.Price = Price

    #CREATE SOME FUNCTIONS
    def StringChanged(self):
        print("CHANGED STRING")

    def Tune(self):
        print("HAPPY BIRTHDAY")

    def Chords(self):
        print("A# + B minor ")


#CREATE OBJECTS AND CALL THE FUNCTIONS
obj1 = Guitar("ROCK","YAMAHA",48000)
print(obj1.StringChanged())
print(obj1.Tune())
print(obj1.Chords())