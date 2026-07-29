print("---------------------------------------------------")
print("-------------Ticket pricing software--------------")
print("---------------------------------------------------")

print("Please enter your age:")
Age = int(input())

if (Age <= 5):
    print("Your ticket is free")
elif(Age > 5 and Age <=18):
    print("Ticket price is 900")
elif(Age >18 and Age <=40):
    print("Ticket price is 1200")
else:
    print("Ticket price is 500")


print("------------------Score---------------------")
print("Please enter score:")
score = int(input())

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



