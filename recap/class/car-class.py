class Car:
    
    def __init__(self, doors, seats, color):
        self.doors = doors
        self.seats = seats
        self.color = color
        
    def Drive(self):
        return f"I have {self.doors} doors, I have {self.seats} seats, the color is: {self.color}."
        

saed = Car(3, 2, "blue")

print(saed.Drive())
