#readlines method in python.
f = open('myfile.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Mark of student {i} in Maths is:{m1}")
    print(f"Mark of student {i} in Science is:{m2}")
    print(f"Mark of student {i} in Physics is:{m3}")

    print("line")

#writelines method in python.
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()