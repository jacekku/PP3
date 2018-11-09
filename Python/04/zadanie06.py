def mediana(tab):
    l=len(tab)
    tab.sort()
    if(l%2==0):
        return (tab[l//2]+tab[(l//2) - 1])/2
    return tab[l//2]

def dominanta(tab):
    out={}
    for num in tab:
        try:
            out[num]+=1
        except KeyError:
            out[num]=1

            #key,value
    max_list=[None,0]
    for key in out:
        if(out[key]>max_list[1]):
            max_list[1]=out[key]
            max_list[0]=key
    return max_list[0]



tab=[2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]


print(f'mediana = {mediana(tab)}')
print(f'dominanta = {dominanta(tab)}')