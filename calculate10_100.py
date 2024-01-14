#Calculate 10^100
import math
import random
from decimal import Decimal,getcontext
def find_x(value):
    print("How many times do you want to calculate?")
    times=input()
    p=20
    getcontext().prec = p
    x = Decimal(random.randint(0,100))
    toptemp=Decimal(100)
    downtemp=Decimal(0)
    t1=Decimal(0)
    t2=Decimal(0)
    for i in range(0,int(times)):
        getcontext().prec = p
        if x**x>value:
            toptemp=x
            x=(toptemp-downtemp)/2+downtemp
            #print(">",end='')
        if x**x<value:
            downtemp=x
            x=(toptemp-downtemp)/2+downtemp
            #print("<",end='')
        if i%5==0:
            print(x)
        if i%2==0:
            t2=x
        if i%2!=0:
            t1=x
        if t1==t2:
            p = p+20
            
find_x(10**100)
input("press enter to exit")