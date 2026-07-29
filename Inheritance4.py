class Base:
    def __init__(self):
        print ("Inside Base constructor:")

    def fun(self):
        print ("Inside Base fun")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print ("Inside derived constructor:")


dobj = Derived()

dobj.fun()