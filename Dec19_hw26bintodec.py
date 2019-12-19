user_input = int(input("enter a binary value"))

bits = list(str(user_input))

decimal = 0

counter = 0

for i in reversed(bits):
    decimal += 2**counter * int(i)
    counter+=1

print("The decimal value is: ", decimal)