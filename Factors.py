def factors(num):
    factors=[]
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter a number:"))
print (f"Factors of {number} are: {factors(number)}")


