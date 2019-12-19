number = int(input("Please Enter any Number: "))

first_digit = number

while (first_digit >= 10):
    first_digit = first_digit // 10
    last_digit = number % 10
print("The sum of first and last digit is",first_digit + last_digit)

