numbers={
    15:"BINGO",
    5:"BAM",
    3:"BIM"
}

for i in range(1,51):
    for n in numbers:
        if(i%n==0):
            print(numbers[n])
            continue
    print(i)
'''


for i in range(1,20):
    if i%3==0 and i%5==0:
        print("BINGO")
        continue
    if i%5==0:
        print("BAM")
        continue
    if i%3==0:
        print("BIM")
        continue
    print(i)
    
'''