n=int(input("Enter number:")) 
d=int(input("Enter digit:" ))
c = 0; 
while (n > 0):  
 if (n % 10 == d): 
  c += 1; 
 n = int(n / 10); 
print("The frequency of the given digit is",c); 