class Human:
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Talk(self):
        return f"I am a human, my name is {self.name}, I am {self.age} years old."
        
saed = Human("saed", 9)

print(saed.Talk())
