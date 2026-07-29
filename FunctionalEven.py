CheckEven = lambda no : (no % 2 == 0)


def main():
    value = int (input("Enter number:"))

    Ret = CheckEven(value)

    if (Ret == True):
        print ("Number is even")
    else:
        print ("Number is odd")

    print (Ret)

if __name__ == "__main__":
    main()

