from snippets import safe_input
user_input=safe_input("Podaj liczbe ")
if(user_input<0):
    print("Liczba {0} jest ujemna".format(user_input))
else:
    print("Liczba {0} jest dodatnia".format(user_input))