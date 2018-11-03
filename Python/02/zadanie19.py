def factorial(n):
    if(n<=1):
        return 1
    else:
        return n * factorial(n-1)


factorials={
    0:1
}

for i in range(1,11):
    factorials[i]=(factorials[i-1]*i)



for i in range(10,-1,-1):
    print("{0}! = {1}".format(i,factorials[i]))


print(factorial(4))