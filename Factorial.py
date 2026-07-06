def main():
    print ("Enter number:")
    N = int(input())
    factorial = 1

    for i in range (1, N+1):
        factorial *= i

    print (f"factorial of number: {factorial}")


if __name__ == "__main__":
    main()