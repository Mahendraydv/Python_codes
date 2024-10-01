#else in a for loop.
for x in range(6):
    print("iteration no.{} in for loop".format(x+1))
else:
    print("else block in loop") 
print("Out of loop")

#if we use break statement else loop not excute.
for x in range(6):
    print("iteration no.{} in for loop".format(x+1))
    if x==4:
        break
else:
    print("else block in loop") 

#else in a while loop.
i = 0
while i<7:
    print(i)
    i = i+1
    if i==4:
        break  

