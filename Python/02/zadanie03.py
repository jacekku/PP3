from snippets import safe_input

a=safe_input("Podaj dzielna: ")
b=safe_input("Podaj dzielnik (nie moze byc zerem (0)): ")
try:
    print("{0}/{1}={2}".format(a,b,a/b))
except ZeroDivisionError:
    print("Dzielenie przez zero")