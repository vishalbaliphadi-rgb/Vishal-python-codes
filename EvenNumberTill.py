def main():
    print ("Enter number:")
    N = int(input())

    print (f"Even numbers till {N}:")
    for i in range (2,N+1,2):
        print (i)          


if __name__ == "__main__":
    main()