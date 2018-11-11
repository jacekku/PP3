def fib(n,start_a=0,start_b=1):
    a,b=start_a,start_b
    for i in range(n-1):
        a,b=b,a+b
    return a

fibs=[0]
for i in range(1,21):
    fibs.append(fib(i))

print(*fibs,sep="\n")