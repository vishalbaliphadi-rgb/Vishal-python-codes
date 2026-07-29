import Marvellous as MI

def main():
    print ("Enter first number:")
    value1 = int(input())

    print ("Enter second number:")
    value2 = int(input())

    ret = MI.Addition (value1 , value2)   
    ret = MI.square (value1)
    
    print ("Addition is:", ret)
    print ("Square", ret)

if __name__ == "__main__":
    main()


