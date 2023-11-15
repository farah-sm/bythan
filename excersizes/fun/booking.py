class Booking:
    "This class represents a booking"
    
    def __init__(self, checkIn, checkOut):
        self.checkIn = checkIn
        self.checkOut = checkOut
        
    def g_checkIn(self):
        return self.checkIn
    
    def g_checkOut(self):
        return self.checkOut  
    
    def overlap(self):
        if self.g_checkOut() > self.g_checkIn() and self.g_checkIn() < self.g_checkOut():
            return True
        else:
            return False
        
    def infoPrint(self):
        return "Date checked in " + self.checkIn() + ", Date checkedout: " + self.checkOut()
    
first_booking = Booking("24/22/2023", "52/22/2023")

print(first_booking.overlap())
