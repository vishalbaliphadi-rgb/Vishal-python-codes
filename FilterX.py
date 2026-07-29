def CheckEven(No):
    return (No % 2 == 0)

def main():
    Data = [13,12,8,10,11,20]

    print ("Input Data is:", Data)

    FData = list(filter(CheckEven, Data))

    print ("Data after filter:", FData)


if __name__ =="__main__":
    main()


#============Repeat===================

def CheckEven1(No):
    return (No% 2 == 0) # Boolean Value check like True or False

def main():

    Data = [11,13,14,16,18]
    print ("Input Data is:", Data)

    FData = list (filter(CheckEven1, Data))
    print ("After filter:", FData)


if __name__ == "__main__":
    main()

#===================Odd=========================

def CheckOdd(No):
    return (No % 2 !=0) 

def main():

    Data = [11,23,44,21,33]
    print ("Input Data is:", Data)

    OData = list(filter(CheckOdd, Data))
    print ("After filter:", OData)


if __name__ == "__main__":
    main()