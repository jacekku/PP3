import math
a=int(input())
b=int(input())
c=int(input())
pole=math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4
print(pole)