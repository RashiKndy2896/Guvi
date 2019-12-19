list=[]
n=int(input("Enter maximum number:" ))
i=1
for i in range(1,n+1):
 if i<n: 
  list.append(i)
i=i+1 
print(list)
print(sum(list))