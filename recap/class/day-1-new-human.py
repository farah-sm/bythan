class Human:
    
    def __init__(self, name, age, city, saying):
        self.name = name
        self.age = age
        self.city = city
        self.saying = saying
    
    def Talk(self):
        return f"Hello world my name is: {self.name}, I am {self.age} years old. I am from {self.city}, My favourite saying is {self.saying}"
        



human2 = Human("Saed", 25, "London", "Lets goooooooooo")


print(human2.Talk())

