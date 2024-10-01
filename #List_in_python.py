#List in python.
list1 = [1, 2, 3, 4, 5]
list2 = ["Red", "Green", "Blue"]
print(list1)
print(list2)

#Accessing list items.
print(list2[2]) #Positive Indexing.
print(list1[-3]) #Negative Indexing.

#Check whether iteam present in the list.
colors = ["Red", "Green", "Yellow", "Blue"]
if "Blue" in  colors:
    print("Blue is present")
else:
    print("Blue is absent")

#Range of Index.
animals = ["cat", "dog", "bat", "horse", "pig", "mouse", "donkey", "monkey", "goat", "cow"]
print(animals[2:8])#using positive index.
print(animals[-7:-2])#using negative index.

#Printing alternative value.
print(animals[::2])#using positive index.
print(animals[-7:-2:2])#using negative index.

#Printing every third value.
print(animals[::3])

#File comprehension.
#print the item smaller letter "0" in the list.
names = ["Milo", "Bruno", "Sarah"]
namesWith_o = [item for item in names if "o" in item]
print(namesWith_o)

#print item more than 4 letters.
namesWith_o = [item for item in names if (len(item)>4)]
print(namesWith_o)

