def power(base,exponent):
    if(exponent<0):
        return 1/power(base,-exponent)
    if(exponent==0):
        return 1
    return base*power(base,exponent-1)

print(power(5,2))
print(power(5,-2))