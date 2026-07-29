import Marvellous1

def main():
    print ("Enter first no.:")
    no1 = int(input())

    print ("Enter Second no:")
    no2 = int(input())

    ret1 = Marvellous1.addition (no1, no2)
    ret2 = Marvellous1.subtraction (no1, no2,)

    print ("Addition:" , ret1)
    print ("substraction:", ret2)

    print ("Enter first string:")
    nam1 = input()

    print ("Enter second string")
    nam2 = input()

    ret3 = Marvellous1.combine (nam1 , nam2)
    print ("Full name:", ret3)

   

if __name__ == "__main__":
    main()