from random import randint as r

def print_IP():
    print(f'{r(0,255)}.{r(0,255)}.{r(0,255)}.{r(0,255)}')

for _ in range(20):
    print_IP()