#importing in python.
import math
result = math.sqrt(9)
print(result)

#from keyword.
from math import sqrt
result = sqrt(9)
print(result)

from math import sqrt, pi
result = sqrt(9) * pi
print(result)

#importing everything.
from math import*
result = float(4) * pi
print(result)

#The "as" keyword.
import math as m
result = m.sqrt(9)
print(result)

#The dir function.
import math
print(dir(math))

