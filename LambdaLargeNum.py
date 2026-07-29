# Largest = lambda a,b,c : max (a,b,c)

# print ("Enter first number")
# ret1 = int(input())
# print ("Enter second number:")
# ret2 = int(input())
# print ("Enter third number:")
# ret3 = int(input())

# Large = Largest(ret1,ret2,ret3)
# print ("Largest number:", Large)


Largest = lambda List : max(List)
smallest = lambda List : min(List)
List = [23,22,56,78,99, 2222]

Large = Largest(List)
small = smallest(List)
print ("Largest number in list:", Large)
print ("Smallest number in list: ", small)




