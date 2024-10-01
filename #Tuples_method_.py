#Manipulating tuples.
countries = ("India", "China", "America", "England", "Russia")
temp = list(countries)
temp.append("Germany")
temp.pop(2)
temp[1] = "America"
countries = tuple(temp)
print(countries)

#Concatenate two tuples.
countries = ("India", "China", "America", "England", "Russia")
States = ("Mumbai", "France")
southAsia = countries + States
print(southAsia)
