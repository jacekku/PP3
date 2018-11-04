from random import randint


def get_bet():
    bet=[]
    for _ in range(6):
        n=randint(1,49)
        while(n in bet):
            n=randint(1,49)
        bet.append(n)
    return bet


for i in range(5):
    print(f'Zaklad {i+1}: ',end="")
    print(*get_bet(),sep=" ")