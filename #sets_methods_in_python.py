#Joining sets in python.
#1.union() and update().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

#update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 ={"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)

#2.intersection() and intersection_update().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

#intersection_update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

#3.symmetric_difference() and symmetric_difference_update().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

#symmetric_difference_update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

#4.difference() and difference_update().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)

#difference_update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.difference_update(cities2)
print(cities) 

#Sets method in python.
#1.isdisjoint().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = { "Seoul", "Kabul"}
print(cities.isdisjoint(cities2))

#2.issuperset().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = { "Tokyo", "Madrid",}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Kabul", "Delhi"}
print(cities.issuperset(cities3))

#3.issubset().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = { "Tokyo", "Madrid",}
print(cities2.issubset(cities))

#4.add()
names = {"Mahendra", "Mishra","Akash"}
names.add("Nel")
print(names)

#5.update().
cars = {"Mustang", "Supra", "Gtr"}
cars2 = {"Maclerin", "Bmw M4"}
cars.update(cars2)
print(cars)

#6.remove() and discard().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

#discard() does not raise error, if item not present in set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Seoul")
print(cities)

#7.pop().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item =cities.pop()
print(cities)
print(item)

#8.del.
#cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
#del cities
#print(cities)

#9clear().
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

#10.Check if item exists.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
if "Berlin" in cities:
    print("Berlin is present")
else:
    print("Berlin is absent")    




