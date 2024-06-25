
from decimal import Decimal

a = 0.1
b = 0.1
c = 0.1
e = 0.3
print(a + b + c) # output 0.30000000000000004

print((a + b + c) - 0.3) # output 5.551115123125783e-17  = problem

# Solution 
d = (Decimal(str(a)) + Decimal(str(b)) + Decimal(str(c))) - Decimal(str(e))
print('value of d : ',d)

# output : value of d :  2.775557561565156540423631668E-17 why ?







print(round((a+b+c)-e)) # 0.0