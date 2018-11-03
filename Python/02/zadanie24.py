from snippets import safe_input
user=1
numbers=[]
while(user!=0):
    user=safe_input("Podaj liczbe: ")
    numbers.append(user)
numbers.pop()
print("Rezultat: Liczb={0}, Suma={1}, Srednia={2}"
.format(len(numbers),sum(numbers),sum(numbers)/len(numbers)))