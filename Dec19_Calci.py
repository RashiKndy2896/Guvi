def add(a,b):
 print(a+b)
def sub(a,b):
 print(a-b)
def mul(a,b):
 print(a*b)
oper = input("Enter the operator:" )
a = int(input("enter a value:"))
b = int(input("enter b value:"))
if oper == 'add':
 add(a,b)
elif oper == 'mul':
 mul(a,b)
elif oper == 'sub':
 sub(a,b)
else:
 print("Enter valid operator")