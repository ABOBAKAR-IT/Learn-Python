x = 2
y = 3
z = 4

print(x + y)
 
 
a = x + y * z # bad practice
print(a)
a = x + (y * z) # good practice

a = 40 + 2.23 # output : 42.23 bad practice
a = float(40 + 2.23) # output : 42.23 good practice
a = int(40 + 2.23) # output : 42 good practice

b = 'rana' + 'abobakar' # concatenate string
print(b)

b = 'rana' + 123 # concatenate Error


# search this keyword

repr('chai')
str('chai')
print('chai')

# comparison in python

result = 1>4 # False

result = 3<4 # True

import math

math.floor(3.5) # output 3
math.floor(-3.5) # output -4


math.trunc(2.8) # output 2
math.trunc(-2.8) # output -2

9999999999999999999999 ** 2.1 # output 2.1e+20

# imagery number
(2 +  1j)* 3 # output (6 + 3j) 


print(0o20) # 16

print(0xFF) # 255

print(0b1000) # 8

oct(64) # '0o40'

hex(64) # 0x40

bin(64) # 0b100000


int(32.2) # 32

int(21,2)
int(32,16)

