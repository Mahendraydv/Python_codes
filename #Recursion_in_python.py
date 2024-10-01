#Factorial numbers.
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return(num*factorial(num-1))

num =7;
print("Numbers:", num)
print("Factorial:",factorial(num))

#Fibonacci series.
def fibonacci (n):
    if (n<=1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter a number:"))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i))
    
