#Add two integers.
def  add(num1: int, num2: int) -> int:
    #Add tow numbers.
    num3 = num1 + num2 

    return num3

num1, num2 = 5, 15
ans = num1 + num2
print(f"The addition of {num1} and {num2} result {ans}.")

#Function to check even or odd.
def  evenOdd(x):
    if(x%2 == 0):
        print("Even")
    else:
        print("Odd")    

evenOdd(255)
evenOdd(10)


