fibs={}
def fib(n):
    if n in fibs:
        return fibs[n]
    if n<2:
        if n==0:
            f=0
        else:
            f=1
    else:
        f=fib(n-1)+fib(n-2)
        fibs[n]=f
    return f



for i in range(20):
    print(fib(i))

print(fibs)