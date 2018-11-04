counter=7
wrap=3
while counter>0:
    print(*range(counter,counter+wrap),sep=" ")
    counter-=wrap