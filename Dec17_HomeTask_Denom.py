amount=int(input("Enter the amount: "))
notes=[2000, 500, 200, 100, 50, 20, 10]
for i in range(7):
 y=notes[i]
 x=int(amount/y)
 amount=int(amount%y)
 print(y, x)         
           
    

