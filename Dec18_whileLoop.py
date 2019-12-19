x = [int(x) for x in input("Enter multiple value: ").split()] 
print("Number of list is: ", x) 
no=int(input("Choose a number: "))
for i in x: 
    if(no in x) : 
        print ("Element Exists") 
        break 
    else:
        print("Element Does not Exist")
        break 
