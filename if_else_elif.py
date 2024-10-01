#if_else statements.
Appleprice = 180
Budget = 120
if(Appleprice <= Budget):
    print("Alexa add one kg apple in the cart.")
else:
    print("Do not buy this apple.")

#elif statements.
num = 0
if(num < 0):
    print("Number is negative")   
elif(num == 0):
    print("Number is zero")
else:
    print("Number is positive")  

#Nested if statements.
num = 22
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Nmuber is between 1to10")
    elif(num > 10 and num <= 20):
        print("Number is between 10to20") 
    elif(num > 20):
        print("Number is gretarthan 20")     
else:
    print("Number is zero")                         

