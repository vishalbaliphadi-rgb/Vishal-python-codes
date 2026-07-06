def main():
    print ("Enter number:")
    N = int (input())

    total = N*(N+1)/2

    print (f"Sum of first {N} natural number is:{total}")

if __name__ == "__main__":
    main()