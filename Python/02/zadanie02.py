from snippets import safe_input

user_input=safe_input("Podaj liczbe: ")
if(user_input%2==1):
    print("Liczba {0} jest nieparzysta".format(user_input))
else:
    print("Liczba {0} jest parzysta".format(user_input))