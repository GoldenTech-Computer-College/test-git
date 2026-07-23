class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def have_birthday(self):
        self.age +=1
        return f"Happy birthday {self.name}! You are now {self.age} years old."

    def greet(self):
        return f"Hello, my name is {self.name}and i am {self.age} years old"     
