#1 Default arguments.
def average(a=5, b=3, c=1):
    print("The average is", a+b+c/2)

average()

#2 Required arguments.
def name(fname, mname, lname):
    print("Hello", fname, mname, lname)

name("Mahendra", "Rajaram", "Yadav")    

#3keyword arguments.
def name(fname, mname, lname):
    print("Hello", fname, mname, lname)

name(mname = "Rajaram", lname = "Yadav", fname = "Mahendra")

#4 Variable argument.
# - Arbitrary aarguments.
def name(*name):
    print("Hello", name[0], name[1], name[2])

name = ("Mahendra", "Rajaram", "Yadav")   
