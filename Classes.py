# Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('Hello, my name is '+str(self.name))

    def change_name(self, new_name):
        self.name = new_name

    def say_age(self):
        print('I am '+str(self.age))
        
p = Person('Simon', 20)
p.say_hi()
p.change_name('Casual')
p.say_hi()

p.say_age()
