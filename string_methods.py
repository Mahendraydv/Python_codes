#1 String to uppercase.
a = "Mahendra"
print(a.upper())

#2 String to lowercase.
print(a.lower())

#3 rstrip to remove any trailing character.
name = "Mahendra!!!"
print(name.rstrip("!"))

#4 Replace one string to another string.
print(a.replace("Mahendra","Mosam"))

#5 Split the given string.
a = "Mahendra Mohit Ram"
print(a.split(" "))

#6 Capitalize turn first character of the string to uppercase.
a = "hey I am Mahendra"
print(a.capitalize())

#7 Center method aligns the string to the center.
a = "Welcome to the console"
print(a.center(50))

#8 Provide padding character.
print(a.center(50,"."))

#9 Count method return the number of given value in the string.
a = "Mahendra"
print(a.count("a"))

#10 endswith method check if the string ends with a given values.
a = "Welcome to the console!!!"
print(a.endswith("!!!"))

#11 Find search value in given string.
a = "He's name is Dan. He is a honest man."
print(a.find("is"))

#12 If value is absent with the use of find().
print(a.find("Daniel"))

#13 Index search value in given string.
print(a.index("Dan"))

#15 If value is absent with the use of index().
#print(a.index("Daniel"))#Give value error.

#16 isalnum() method return true if the string only consists of A-Z, a-z, 0-9, otherwise return false.
a = "WelcomeToTheConsole"
print(a.isalnum())

#17 isalpha() method return true if the string only consists of A-Z, a-z,  otherwise return false.
a = "Welcome1"
print(a.isalpha())

#18 islower() returns true if all the charcters in the string are lower case.
a = "hello world"
print(a.islower())

#19 isprintable() method returns true if alll the values printable in given string otherwise return false.
a = "We wish you a Merry Christmas \n" # \n is not printable 
print(a.isprintable())

#20 isspace() method returns true only and only if the string contains white spaces.
a = "  " #using spacebar.
print(a.isspace())

b = "       " #using Tab
print(a.isspace())

#21 istitle() return true if the first letter of each word is capitalized.
a = "World Health Organization"
print(a.istitle())

#22 title() method capatalizes each letter of the word within the string.
a = "world health organization"
print(a.title())

#23 isupper() returns true if all the characters in the string are uppercase otherwise retuen false.
a = ("WORLD HEALTH ORGANIZATION")
print(a.isupper())

#24 startswith() method checks if the string starts with a given value then return true, otherwise return false.
a = ("Python is a interpeted")
print(a.startswith("Python"))

#25 swapcase() method change the character casing of the string. uppercase converted to lowercase and lowercase to uppercase.
a = ("Python is a Interpreted Language")
print(a.swapcase())