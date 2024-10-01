#seek() function in python.
with open('text.txt', 'r') as f:
    print(type(f))

#Move to the 10byte in the file.
f.seek(10)

#read the next 5bytes.
print(f.tell())#tell() function.
data = f.read(5)
print(data)

#truncate() function in python.
with open ('text.txt', 'w') as f:
    f.write('Hello world!')
    f.truncate(5)

    with open('text.txt', 'r') as f:
        print(f.read())

