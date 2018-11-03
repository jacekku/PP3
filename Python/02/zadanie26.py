def print_square(a=1,b=1,char="*"):
    #top
    print(char*b)
    #middle
    for i in range(a-2):
        print("{0}{1}{2}"
        .format(char," "*(b-2),char))
    #bottom
    print(char*b)


import snippets as s
a=s.safe_input("Podaj a: ")
b=s.safe_input("Podaj b: ")
print_square(a,b)