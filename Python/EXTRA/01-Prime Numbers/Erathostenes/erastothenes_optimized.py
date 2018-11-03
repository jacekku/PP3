from time import time

def erathostenes(limit,ret=False):
    limit=int(limit)
    def set_prime(number,is_prime):
        primes[number]=is_prime


    def is_prime(number,flip=False):
        if(flip):
            primes[number]=not primes[number]
        return primes[number]

    primes=list([True]*limit//2)
    i=3
    while i*i<limit:
        if(is_prime(i//2)):
            j=i*i
            while j<limit:
                set_prime(j//2,False)
                j+=i*2
         i+=2
        
    if(ret):
        return primes

def time_erathostenes(limit):
    START=time()
    erathostenes(limit)
    return time()-START

def make_times_list(limit,list_size=20):
    return [limit]+[time_erathostenes(limit) for i in range(list_size)]



#  2  3  5  7  11  13  17  19  23  29  31  37  41  43  47
'''l=[10,25,50]
count=1
for i in range(2,9):
    for n in l:
        limit=n*10**i
        if(limit<5000000000):
            print(f'{count}: limit={limit} time={time_erathostenes(limit)}') 
        count+=1'''