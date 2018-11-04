from random import randint

#     even odd
sums=[  0,  0]
for _ in range(1000):
    num=randint(1,50)
    sums[num%2]+=1

print(f'Liczby parzyste: {sums[0]/1000 * 100}%')
print(f'Liczby nieparzyste: {sums[1]/1000 *100}%')