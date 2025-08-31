class Baba :
    car='BMW'
    taka= '1000 core'
    home = '10 Floor'


class kaka(Baba): 
    BrokernPhone=''
    BrokenHome=''


k = kaka()
print(k.home)


class Person:
    def __init__(self , fname , lnmame ):
        self.firstname = fname
        self.lastname = lnmame
        pass
    def printname(self):
        print(self.firstname , self.lastname)
    def __str__(self):
        return f"Student fName: {self.firstname}, lastname: {self.lastname}"

x = Person('swapnil' , 'ahmed shishir')
x.printname()
print(x)