# class MyClass:
#     name:'s'
#     age:'a'

# z = MyClass()
# z.name = 'swapnil'
# print(z.name)

class Person:
    def __init__(self , name , age ,subject):
        self.name= name
        self.age = age
        self.subject=subject

p1 = Person('swapnil' , 34)
print(p1.name)
print(p1.age)