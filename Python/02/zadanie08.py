from snippets import safe_input

def check_gender(gender_string):
    return "M" if int(gender_string)%2==1 else "F"

def check_year(year_string,month_string):
    centuries={
        "0":1900,
        "1":1900,
        "2":2000,
        "3":2000,
        "4":2100,
        "5":2100,
        "6":2200,
        "7":2200,
        "8":1800,
        "9":1800,
    }
    year=centuries[month_string[0]]
    year+=int(year_string)
    return year

PESEL=""
while(len(PESEL)!=11):
    PESEL=str(safe_input("Podaj prawidlowy PESEL: ","PESEL musi byc liczba"))
check_obj={
    "year":PESEL[0:2],
    "month":PESEL[2:4],
    "day":PESEL[4:6],
    "serial":PESEL[6:10],
    "gender":PESEL[9],
    "control":PESEL[10]
}
#for v in check_obj:
#    print("{0} : {1}".format(v,check_obj[v]))
print("Rok: {0}".format(check_year(check_obj["year"],check_obj["month"])))
print("Płeć: {0}".format(check_gender(check_obj["gender"])))