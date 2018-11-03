odds=0
evens=0
for i in range(1,51):
    if(i%2==0):
        evens+=i
    else:
        odds+=i

print("evens: {0} odds: {1}".format(evens,odds))

