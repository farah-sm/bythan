class Guest:
    "This class represents a room in a hotel, we need to implement enumerate type, fro size of hotel room, must be single, double, tripple"
    name = ''
    age = ''
    nationality = ''
    mobile = 0
    id = False
    
    def __init__(self, name, age, nationality, mobile, id) :
        self.name = name
        self.age = age
        self.nationality = nationality
        self.mobile = mobile
        self.id = id
        
    def getGuestInfo(self): 
        details = "Guest Name: " + str(self.getName()) + ", " + self.name + "'s age is: " + str(self.getAge()) + ", The Guest is from: " + str(self.getNationality()) + ", Mobile Number: " + str(self.getMobile()) + ", Is there ID: " + str(self.getId())  + "."
        return details
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    def getMobile(self):
        return self.mobile
    
    def getId(self):
        return self.id
    
    def getNationality(self):
        return self.nationality
    
    
Guest1 = Guest("Faisal", 47, "Somaliland", 7288888888, True)

print(Guest1.getGuestInfo())


