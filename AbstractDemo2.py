from  abc import ABC,abstractmethod

class Base(ABC):
    @abstractmethod
    def Addition (self, no1, no2):
        pass

class Derived(Base):
    def Addition (self, no1, no2):
        return no1 + no2


dobj = Derived() 
your_age = 10
Ret = dobj.Addition(10,11)
print ("Addition is:", Ret)
a = int(input(your_age))
print ("age", a)
