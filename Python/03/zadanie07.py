f=open("Numbers.txt")
numbers=f.read().split(",")
suma=0
for number in numbers:
    suma+=int(number)

print(suma)

f.close()