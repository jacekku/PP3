PIN="0805"
counter=3
while(counter>0):
    USER_PIN=input("Podaj PIN: ")
    if(PIN!=USER_PIN):
        print("PIN nieprawidlowy")
        counter-=1
        continue
    if(PIN==USER_PIN):
        print("PIN prawidlowy, witamy")
        exit()
print("Karta platnicza zostaje zablokowana")