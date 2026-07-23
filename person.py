class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def have_birthday(self):
        self.age +=1
        return f"happy birthday! you are now {self.age} years old."