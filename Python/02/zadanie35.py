def print_calendar_header(days):
    for day in days:
        print(f'| {day} ',end="")
    print("|")

def print_empty_days_at_head(days):
    if(days):
        print("|    "*days,end="")


def print_empty_days_at_tail(days):
    if(days):
        print("|    "*days,end="|\n")

def print_month(days,number_of_days,start_day):
    start_day%=7
    print_calendar_header(days)
    print_empty_days_at_head(start_day)

    counter=start_day
    for day in range(1,number_of_days+1):
        print(f'| {day:2} ',end="")
        counter+=1
        if(counter%7==0):
            print("|")
        
    print_empty_days_at_tail(7-(counter%7) if counter%7 else None)
    print()
 
    
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
print_month(days,num_of_days,start_day)
