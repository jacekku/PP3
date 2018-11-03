import snippets as s

number = s.safe_input("Podaj liczbe: ")
for i in range(1,11):
    print("{0} x {1} = {2}".format(number,i,i*number))