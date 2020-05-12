#!/usr/bin/env python3
a = 1
print('-'*50)
while a < 11:
    b = 1
    while b < 11:
        print('{:5d}'.format(a*b),end=' ')
        b += 1
    a += 1
    print()
print('-'*50)
    
