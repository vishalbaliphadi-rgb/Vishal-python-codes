def CheckEven(No):
    return (No % 2 == 0)

#CheckEven = lambda No : (No% 2 == 0) # lambda use
# Increment = lambda No : (No)

def Increment(No):
    return No + 1

def main():
    Data = [13,12,8,10,11,20]

    print ("Input Data is:", Data)

    FData = list(filter(CheckEven, Data))

    print ("Data after filter:", FData)

    MData = list(map(Increment, FData))

    print ("Data after map:", MData )


if __name__ =="__main__":
    main()


print("=============Repeat==================")
def CheckEven2(No):
    return (No %2 == 0) 

def Increment2(No):
    return No + 2

def main():
    Data = [11,12,13,14,15]
    print ("Input data:", Data)

    FData = list (filter(CheckEven2, Data)) 
    print ("Filtered Data:", FData)

    MData = list (map(Increment2, FData))
    print ("Mapped Data:", MData)
    


if __name__ == "__main__":
    main()
