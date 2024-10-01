tup1 = (1,2,3,4)
tup2 = ("Arrays", "Output")
print(tup1)
print(tup2)

print(tup1[0])#Positive index.
print(tup1[-3])#Negative index.

if "Arrays" in tup2:  #Check for item.
    print("Arrays is present")
else:
    print("Arrays is absent")  

print(tup1[1:3])#Range of index.
print(tup1[0:5:2])#Jump index.


