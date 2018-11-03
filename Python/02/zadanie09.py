from snippets import safe_input

numbers=[
    safe_input("Podaj pierwsza liczbe: "),
    safe_input("Podaj druga liczbe: "),
    safe_input("Podaj trzecia liczbe: "),
]
numbers.sort() #in-place FUJ
print("Mediana wynosi {0}".format(numbers[1]))