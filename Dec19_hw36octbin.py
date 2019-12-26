import math
def octal_to_binary(octal):
decimal = 0
i = 0
binary = 0
while(octal != 0):
decimal += (octal%10) * math.pow(8,i)
i = i + 1
octal = int (octal / 10)

i = 1

while (decimal != 0):
binary = binary + (decimal % 2) * i;
decimal = int(decimal / 2);
i *= 10;

return binary

octal = int(input(“Enter an octal number : “))
print(“Binary Equivalent : “,int(octal_to_binary(octal)))
