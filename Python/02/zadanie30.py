from snippets import safe_input

number=safe_input("Podaj liczbe: ",convert_to_int=True)
number_binary=[number]
while(number_binary[0]!=1):
    number_binary.append(number_binary[0]%2)
    number_binary[0]//=2


print("{0}(10)=".format(number),end="")
print(*number_binary,sep="",end="(2)\n")