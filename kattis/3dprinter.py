#3dprinter
#https://open.kattis.com/problems/3dprinter
import math
def days(n):
    printers = 1
    d = 0
    while printers < n:
        printers *= 2
        d += 1
    return d + 1
    

while True:
    
    n = int(input())
    print(days(n))


