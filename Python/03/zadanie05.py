f=open("NoEducation.txt")
for line in f:
    print(f'{len(line)} {line}',end="")
f.close()