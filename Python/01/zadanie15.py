import random as r
answer=-1
throw=r.randint(1,6)
while(answer != throw):
    answer=-1
    try:
        while(answer<1 or answer>6):
            answer=int(input("Type a number between 1 and 6 "))
    except TypeError:
        print("Please enter a number")
    
print(True)