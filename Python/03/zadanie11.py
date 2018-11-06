f=open("Powers.txt","w")

out=""
for i in range(1,11):
    out+=f'{i:2} {i**2:3} {i**3:4}\n'
f.write(out)
f.close()