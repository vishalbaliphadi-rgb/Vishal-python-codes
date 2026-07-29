class Demo:
    def __init__(self, A):
        self.no = A

    def __add__(self, other):
        return self.no + other.no

    def __sub__(self, other):
        return self.no - other.no
    
    def __mul__(self, other):
        return self.no * other.no
    
    def __truediv__(self, other):
        return self.no / other.no


obj1 = Demo(11)
obj2 = Demo(21)

print (obj1 + obj2) #obj1.__add__(obj2)---> _add__(obj1,obj2)
print (obj1 - obj2) #obj1.__sub__(obj2)---> _add__(obj1,obj2)
print (obj1 * obj2) #obj1.__add__(obj2)---> _add__(obj1,obj2)
print (obj1 / obj2) #obj1.__add__(obj2)---> _add__(obj1,obj2)