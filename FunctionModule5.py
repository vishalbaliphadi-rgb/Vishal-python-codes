from Marvellous import *

def main():
    print ("Enter first number:")
    value1 = int(input())

    print ("Enter second number:")
    value2 = int(input())

    ret = Addition (value1 , value2)   
    print ("Addition: ", ret)

    ret = Substraction (value1 , value2)   
    print ("Substraction is:", ret)

    


if __name__ == "__main__":
    main()


