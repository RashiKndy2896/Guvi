odd=[]
even=[]
n=int(input("Enter the maximum value: "))
i=1
for i in range(1,n+1):
 if i%2 == 0:
  even.append(i)
 else:
  odd.append(i)
print(odd)
print(sum(odd))