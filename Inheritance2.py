class Base:
    def __init__(self):
        print ("Inside Base constructor:")

class Derived(Base):
    def __init__(self):
        print ("Inside derived constructor:")


bobj1 = Base()