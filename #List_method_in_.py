#List.sort() the method sorts the list in asceding order.
colors = ["Yellow", "Green", "Blue", "White"]# using string.
colors.sort()
print(colors)
num = [4,5,9,0,2,7,1,5,6,3,1,]# using integer.
num.sort()
print(num)

#You want to print list in descending order.
#colors = ["Yellow", "Green", "Blue", "White"]# using string.
#colors.sort()(reverse = True)
#print(colors)
#num = [4,5,9,0,2,7,1,5,6,3,1,]# using integer.
#num.sort()(reverse = True)
#print(num)

#Reverse() this method reverse the order of the list.
colors = ["Yellow", "Green", "Blue", "White"]# using string.
colors.reverse()
print(colors)
num = [4,5,9,0,2,7,1,5,6,3,1,]# using integer.
num.reverse()
print(num)

#Index() this method return the index of the first occurenceof the list items.
colors = ["Yellow", "Green", "Blue", "White"]# using string.
print(colors.index("Green"))
num = [4,5,9,0,2,7,1,5,6,3,1,]# using integer.
print(num.index(9))

#Count() Returns the count of the number of items with the given value.
colors = ["Yellow", "Green", "Blue", "White"]# using string.
print(colors.count("Green"))
num = [4,5,9,0,2,7,1,5,6,3,1,]# using integer.
print(num.count(1))

#Copy() Return copy of the list.
colors = ["Yellow", "Green", "Blue", "White"]
newlist = colors.copy()
print(colors)
print(newlist)

#Append() this method append item to the end of the list.
colors = ["Yellow", "Green", "Blue", "White"]
colors.append("Red")
print(colors)

#Insert() this method insert a item at the given index.
colors = ["Yellow", "Green", "Blue", "White"]
colors.insert(2,"Red")
print(colors)

