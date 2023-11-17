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
            return "This date is invalid"
        else:
            return "Success, these dates are correct"
        
    def infoPrint(self):
        return "Date checked in " + str(self.g_checkIn()) + ", Date checkedout: " + str(self.g_checkOut())
    
first_booking = Booking("04/08/2025", "00/04/2030")

print(first_booking.overlap())
