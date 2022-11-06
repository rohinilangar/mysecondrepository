class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

p2 = Person("Rohini", 26)
p2.myfunc()