'''numbers={}
for i in range(2,7):
    numbers[i]=0
counter=7
while(0 in numbers.values()):
    for i in numbers:
        if(numbers[i]==0):
            if(counter%i==1):
                numbers[i]=counter
    counter+=7

print(numbers)'''


7 

2,3,4,5,6 == 1

counter=7
while True:
    only_ones=True
    for i in range(2,7):
        if(counter%i!=1):
            only_ones=False
            break
    if(only_ones):
        break
    counter+=7
print(counter)
