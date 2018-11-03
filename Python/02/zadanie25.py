import random
numbers={}
for i in range(1,7):
    numbers[i]=0
for i in range(100):
    numbers[random.randint(1,6)]+=1

words={
    1:"Jedynka",
    2:"Dwójka",
    3:"Trójka",
    4:"Czwórka",
    5:"Piątka",
    6:"Szóstka",
}

for i in numbers:
    print("{0}: {1}"
    .format(words[i],numbers[i]))