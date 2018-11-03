
from snippets import safe_input

dog_age=safe_input("Podaj wiek psa: ")
first_year=10.5
first_year_years=2
next_year=4
age_in_human_years=0
if(dog_age-2>0):
    age_in_human_years=first_year*first_year_years
    age_in_human_years+=(dog_age-2)*next_year
else:
    age_in_human_years=-(dog_age-2)*first_year

print("Wiek psa w ludzkich latach to {0} lata".format(age_in_human_years))