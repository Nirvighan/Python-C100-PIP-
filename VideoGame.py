
# CREATE A CLASS
class VideoGame(object):
    #CREATE CONSTRUCTOR __INIT__
    def __init__(self,name,price,launchDate):
        self.name = name
        self.price = price
        self.launchDate = launchDate
    
    # CREATE SOME FUNCTIONS
    def Start(self):
        print('GAME STARTED')

    def Character(self):
        print('CHOOSE YOUR CHARACTER')

    def Mission(self):
        print("MISSION 1")

    def Stop(self):
        print('MISSION COMPLETED ')
        print('GSME STOP')

#CREATE OBJECTS
game1 = VideoGame("Ghost recon Breakpoint",1200,2018)


# CALL AND PRINT THE FUNCTIONS
print(game1.Start())
print(game1.Character())
print(game1.Mission())
print(game1.Stop())