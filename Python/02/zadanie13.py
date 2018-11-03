from math import sqrt
from snippets import safe_input

a=safe_input("Podaj a ")
b=safe_input("Podaj b ")
c=safe_input("Podaj c ")
roots=[]
print("{0}x^2 + {1}x + {2} = 0".format(a,b,c))
if(a==0):
    roots.append(-(c/b))
else:
    delta=b**2-4*a*c
    if(delta<0):
        print("Brak pierwiastkow rzeczywistych")
        exit()
    if(delta==0):
        roots.append((-1*b)/(2*a))
    else:
        delta_sqrt=sqrt(delta)
        roots.append(((-1*b)+delta_sqrt)/2*a)
        roots.append(((-1*b)-delta_sqrt)/2*a)

print(*roots,sep="\n")