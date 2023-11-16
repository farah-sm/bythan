class Room:
    "This class represents a room in a hotel, we need to implement enumerate type, fro size of hotel room, must be single, double, tripple"
    booking = []
    number = 0
    floor = 0 
    cost = 0
    
    
    
    
    def __init__(self, number, floor, cost):
        self.number = number
        self.floor = floor
        self.cost = cost
        
        
        
        
    def getRoomInfo(self):
        details = "Room Number: " + str(self.getNumber()) + ". The Room is on floor: " + str(self.getFloor()) + ". The room costs: £" + str(self.getCost()) +"."
        
        
        return details


    def getFloor(self):
        return self.floor
    
    
    def getNumber(self):
        return self.number
    
    
    def getCost(self):
        return self.cost
    
SaedsRoom = Room(12, 3, 89.99)
    
print(SaedsRoom.getRoomInfo())
    
