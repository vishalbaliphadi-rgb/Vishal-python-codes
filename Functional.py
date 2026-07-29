addition= lambda no1, no2 : no1+no2

substraction= lambda no1, no2: no1 - no2

print ("Enter first number:")
Value1 = int(input())

print ("Enter Second number:")
Value2 = int(input())

ret = addition(Value1, Value2)

print ("Addition is:", ret)

ret = substraction(Value1, Value2)

print ("substraction is:", ret)