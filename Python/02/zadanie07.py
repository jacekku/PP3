from snippets import safe_input


user=safe_input("Podaj wiek: ")
if(user>120 or user<18):
    print("Podany wiek jest nieprawidlowy")
else:
    print("Podany wiek jest prawidlowy")