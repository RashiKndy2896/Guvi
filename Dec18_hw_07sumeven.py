even=[]
n=int(input("Enter the maximum value: "))
i=1
while i in range(1,n+1):
 if i%2 == 0:
  even.append(i)
 i=i+1
print(even)
print("Sum of even is:",sum(even))