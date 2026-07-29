from  abc import ABC,abstractmethod

class Base(ABC):
    @abstractmethod
    def Addition (self, no1, no2):
        pass

class Derived(Base):
    pass


dobj = Derived() #Error