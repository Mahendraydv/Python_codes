#Raising custom error.
a = int(input("Enter any value between 5 and 9:"))
if(a<5 or a>9):
     raise ValueError("Value should betwwen 5 and 9")

#Quick qize.
a = input("Enter any value between 5 and 9:")
if a == "quit":
    print("Program executed")
else:    
    raise ValueError("Value should betwwen 5 and 9")

