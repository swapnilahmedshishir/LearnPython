class className:
    def InstantMethod(self):
        print("Hellow Instant Method")
    
    @classmethod
    def ClassMethod(cls):
        print('This is a Class Method')


v1 = className()
v1.InstantMethod()
className.ClassMethod()