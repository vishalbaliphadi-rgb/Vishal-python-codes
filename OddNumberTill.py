def main():
    print ("Enter Number:")
    N = int(input())
   
    print (f"Odd numbers till {N}:")
    for i in range (1,N+1,2):
        print (i, end =" ")


if __name__ == "__main__":
    main()