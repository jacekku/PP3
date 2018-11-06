tab_size=10
tab=list([0 for i in range(tab_size)]for j in range(tab_size))

for i in range(len(tab)):
    tab[i][i]=1
print(*tab,sep="\n")