f=open("NoEducation.txt")
i=1
for line in f:
    print(f'{i} {line}',end="")
    i+=1
f.close()