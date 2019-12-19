odd=[]
even=[]
x = [int(x) for x in input("Enter multiple value: ").split()] 
print("Number of list is: ", x) 
for i in x:
 if(i%2 == 0):
  even.append(i)
 else:
  odd.append(i)
print(even)
print(odd)
print("Sum of elements in Odd list is :", sum(odd))
print("Sum of elements in Even list is :", sum(even))  