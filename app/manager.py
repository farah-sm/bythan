from room import *



# Key is Room Number and value is the Room object.
roomDict = {
    int, Room
}

def bookRoom(self, roomNumber, room_obj):
    self._room = room_obj 
    
    self.roomNumber = roomNumber
    
    if self.roomNumber not in roomDict():
        return False
    
    
    room = roomDict[roomNumber]
    
    return room.addRoom(self._room)
        


        
def addRoom(self, room_obj):
    self._room = room_obj
    roomNumber = self.room.getNumber()
    
    if roomNumber not in roomDict:
        roomDict.add(roomNumber, self._room)
    else:
        False
        
class Manager:
    
    roomDict = {
    int, Room
}
    
    
    