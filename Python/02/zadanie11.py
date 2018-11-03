from snippets import safe_input

limit_fines={
    "soft":{"limit":10,"fine":5},
    "hard":{"limit":None,"fine":15}
}

limit = safe_input("Podaj limit predkosci (km/h) ")
velocity = safe_input("Podaj predkosc pojazdu (km/h) ")
difference = velocity-limit

over_soft_limit = 0 if difference<limit_fines["soft"]["limit"] else difference-limit_fines["soft"]["limit"]



if(over_soft_limit):
    fine=   (over_soft_limit)           *limit_fines["hard"]["fine"]
    fine+=  limit_fines["soft"]["limit"]*limit_fines["soft"]["fine"]
else:
    fine=difference*limit_fines["soft"]["fine"]

print("Mandat: {0}".format(fine))