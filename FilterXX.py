CheckEven = lambda No : (No % 2 ==0)


def main():
    Data = [13,12,8,10,11,20]

    print ("Input Data is:", Data)

    FData = list(filter(CheckEven, Data))

    print ("Data after filter:", FData)


if __name__ =="__main__":
    main()


CheckSquare = lambda No1 : (No1*No1)

def main():
    Data1 = [10, 2, 4, 6]
    print ("Input data is", Data1)

    Fdata1 = list (map(CheckSquare, Data1))
    print ("Data after filter", Fdata1)

if __name__ == "__main__":
    main()

