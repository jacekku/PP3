def print_sideways_piramid(size=1,char="*"):
    for i in range(size//2):
        print(char*(i+1))
    for i in range(size//2+1,0,-1):
        print(char*i)



print_sideways_piramid(7)