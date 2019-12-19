def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
  
a = int(input("enter a value:"))
b = int(input("enter b value:"))
  

print ("The gcd is : ",end="") 
print (computeGCD(a,b)) 