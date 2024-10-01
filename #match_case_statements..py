x = int(input("Enter the value of x:"))
# x is the variable to match.
match x:
        case 0:
                print("x is zero ")
        case 4:
                print("case is 4")
        case _:
                print(x)                