#Exception Handling.
a = (input("Enter a number: "))
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i}= {int(a) * i}")
except Exception as e:
  print(e)    

print("Some important line of code")
print('End of program')    

#Invalid integer.
try:
  num = int(input("Enter an integer:"))
except ValueError:
  print("Number entered is not an integer.")  