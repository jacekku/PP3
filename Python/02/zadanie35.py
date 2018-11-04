def print_calendar_header(days):
    for day in days:
        print(f'| {day} ',end="")
    print("|")

def print_empty_days(start_day):
    print("|    "*start_day,end="")

def print_calendar(days,number_of_days,start_day):
    start_day%=7
    print_calendar_header(days)
    print_empty_days(start_day)

    counter=start_day
    for day in range(1,number_of_days+1):
        print(f'| {day:2} ',end="")
        counter+=1
        if(counter%7==0):
            print("|")
        
    print_empty_days(6-start_day)
days=[
    "PN",
    "WT",
    "SR",
    "CZ",
    "PT",
    "SB",
    "ND"
]
num_of_days=30
start_day=2

print_calendar(days,num_of_days,start_day)