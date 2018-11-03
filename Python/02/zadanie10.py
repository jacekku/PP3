from snippets import safe_input

numbers=[
    safe_input("Podaj pierwsza liczbe: "),
    safe_input("Podaj druga liczbe: "),
    safe_input("Podaj trzecia liczbe: "),
]
numbers.sort()
print("Liczby w kolejnosci rosnacej ",end="")
print(*numbers,sep=" ")