maximum = int(input(" Please Enter the Maximum Value: "))

def factorial(number): 
  
    fact = 1
      
    if number == 0 or number == 1 : 
        return fact 
      
    for i in range(2, number + 1) : 
        fact *= i 
      
    return fact 

for Number in range(1, maximum):
    Temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10
    
    if (Sum == Number):
        print(" %d is a Strong Number" %Number)