"""
Encapsulation means hiding the internal details of how something works and only showing the important stuff to the outside world.

Think of it like this:

You drive a car without needing to know how the engine works inside.

You just:

Use the steering wheel

Press the pedals

Watch the dashboard
"""
class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

s1 = Student("Rahul", 21)
print(s1.name)  
print(s1.age) 

#You can access and change name and age from outside the class.
#These are public — NOT encapsulated.  

#above the method is normal now using the encapsluation

