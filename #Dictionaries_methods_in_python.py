#Dictionaries methods in python.
#Update() iteam in dictionary.
info = {'name':'karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20, 'DOB':2001})
print(info)

#Removing items from dictionary.
#clear() for remove all item in dictionary.
info = {'name':'karan', 'age':19, 'eligible':True}
info.clear()
print(info)

#pop() remove particular item.
info = {'name':'karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#popitem() remove automatically last item in dictionary.
info = {'name':'karan', 'age':19, 'eligible':True, 'DOB':2001}
info.popitem()
print(info)

#del remove whole dictionary.
info = {'name':'karan', 'age':19, 'eligible':True}
del info
print(info)
