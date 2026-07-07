def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10   # extract last digit
        total += digit     # add to total
        num //= 10         # remove last digit
    return total

# Accept input from user
number = int(input("Enter a number: "))
print(f"Sum of digits of {number} is: {sum_of_digits(number)}")


