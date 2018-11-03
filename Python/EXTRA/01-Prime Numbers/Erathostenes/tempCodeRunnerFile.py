
power=2
limit=10**power
out=erathostenes(limit,True)
file=open(f'primes-10e{power}',"w")
for i in range(2,limit):
    if(out[i]):
        file.write(f'{i}\n')
file.close()