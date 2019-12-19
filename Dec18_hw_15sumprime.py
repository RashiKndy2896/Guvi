prime=[]
upper = int(input("Enter upper range: "))  
  
for num in range(1,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else: 
           prime.append(num)
print(prime)
print("Sum of prime values is",sum(prime))            