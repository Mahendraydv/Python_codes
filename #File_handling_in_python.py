#Reading file.
f = open('text.txt', 'r')
contents = f.read()
print(contents)

#Writing file.
f = open('text.txt', 'w')
f.write('Hello, world')

#Append a file.
f = open('text.txt', 'a')
f.write('Hello, world')

#Closing a file.
f = open('myfile.txt', 'r')
# ... do something with the file
f.close()

#The 'with' statement.
# with open('myfile.txt', 'r') as f:
    # ... do something with the file
