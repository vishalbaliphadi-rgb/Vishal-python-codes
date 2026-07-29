import Marvellous

def main():
    print ("Enter first number:")
    value1 = int(input())

    print ("Enter second number:")
    value2 = int(input())

    ret1 = Marvellous.Addition (value1 , value2)   
    ret2 = Marvellous.square (value1)
    
    print ("Addition is:", ret1)
    print ("Square:", ret2)

if __name__ == "__main__":
    main()


