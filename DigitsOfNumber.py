def main():

    print ("Enter number:")
    N = int(input())
    
    digits = len(str(N)) # Typecasting from integer to string to check digits
    print (f"Number of digits: {digits}")

if __name__ == "__main__":
    main()