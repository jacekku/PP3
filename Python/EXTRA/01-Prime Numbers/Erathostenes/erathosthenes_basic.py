from time import time

def erathostenes(limit,ret=False):
    limit=int(limit)
    def set_prime(number,is_prime):
        primes[number]=is_prime


    def is_prime(number,flip=False):
        if(flip):
            primes[number]=not primes[number]
        return primes[number]

    primes=list([True]*limit)
    i=2
    while i*i<limit:
        if(is_prime(i)):
            j=i*i
            while j<limit:
                set_prime(j,False)
                j+=i
        i+=1
        
    if(ret):
        return primes

def time_erathostenes(limit):
    START=time()
    erathostenes(limit)
    return time()-START

def make_times_list(limit,list_size=20):
    return [limit]+[time_erathostenes(limit) for i in range(list_size)]




#  2  3  5  7  11  13  17  19  23  29  31  37  41  43  47
