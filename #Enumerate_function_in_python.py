#Enumerate function in python.
fruits = ('apple', 'banana', 'mango')
for index, fruit in enumerate(fruits):
    print(index, fruits)


marks = [12, 34, 45, 98, 66, 45]
for index, mark in enumerate(marks, start=1):
    print(marks)
    if(marks == 3):
        print("Awesome!, Mosam")