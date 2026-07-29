from MarvellousLibrary import filterX, mapX, reduceX

CheckEven = lambda No: (No %2 == 0)
Increment = lambda No: (No +1)
Addition = lambda No1 , No2 : No1 + No2

def main():

    Data = [13,12,8,10,11,20]
    print ("Input Data is:", Data)

    FData = list(filterX(CheckEven, Data))
    print ("Data after filter", FData)

    MData = list (mapX(Increment, FData))
    print ("Mapped Data:", MData)

    RData = reduceX (Addition , MData)
    print ("Reduced Data:", RData)




if __name__ == "__main__":
    main()