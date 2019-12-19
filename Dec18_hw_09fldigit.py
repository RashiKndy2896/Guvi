number = int(input("Please Enter any Number: "))

first_digit = number

while (first_digit >= 10):
    first_digit = first_digit // 10
    last_digit = number % 10
print(first_digit)
print(last_digit)
