n = int(input("Enter the Binary no:" ))
list = [int(x) for x in str(n)]
print(list)
for i in range(0,len(list)):
 if i == 0:
  i = 1
 else:
  i = 0
print(list)