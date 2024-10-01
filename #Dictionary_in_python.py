info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

#Accessing Dictionary items:
#1.Accessing single values.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])#if item not present, they raised error.
print(info.get('name'))#if item not present, they not raised error.

#2.Accessing multiple values.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

#3.Accessing key.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

#4.Accessing key-values.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())