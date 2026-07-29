#def factors(num):
#    factors=[]
#    for i in range(1,num+1):
#        if num % i == 0:
#            factors.append(i)
#    return factors

#number = int(input("Enter a number:"))
#print (f"Factors of {number} are: {factors(number)}")



def factor1(num):
    factor2=[]
    for i in range(1 , num+1):
        if num % i == 0:
            factor2.append(i)
    return factor2

number = int(input("Enter a number:"))
print (f"factors of {number} are: {factor1(number)}")



