f=open("zadanie10.txt","w")
tab=[32,16,5,8,24,7]
tab=map(lambda x:f'{str(x)}\n',tab)
f.writelines(tab)
f.close()