user_data={
    "login":"marek",
    "password":"m-123"
}
login=input("Podaj login: ")
password=input("Podaj haslo: ")
if(login==user_data["login"] and password==user_data["password"]):
    print("Jestes zalogowany")
else:
    print("Podane dane sa nieprawidlowe")