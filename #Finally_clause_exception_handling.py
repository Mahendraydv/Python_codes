#Finally clause in exception handling.
try:
    num = int(input("Enter an integer:"))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")         

#Finally clause in functions in python.
def func1():
    try:
        l = [1,3,4,5]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print('Some error occured')
        return 0
    finally:
        print("I am always executed")

x = func1()
print(x)        
