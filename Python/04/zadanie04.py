"""
DATA

Java :      61K
Python:     47K
JavaScript: 37K
C++:        32K
C#:         26K
Ruby:       18K
Perl:       14K
PHP:        14K
C:          9K
Android:    7K
Graph max:  75K

"""

# two lists implementation as stated in the excercise
languages=[
    "Java",
    "Python",
    "JavaScript",
    "C++",
    "C#",
    "Ruby",
    "Perl",
    "PHP",
    "C",
    "Android"
]

values=[
    61,47,37,32,26,18,14,14,9,7
]
max_value=max(*values)
longest_name=len(max(*languages,key=len))
max_graph_height=40 # arbitrary
print("---Two Lists---")
for i in range(len(languages)):
    percentage=int((values[i]/max_value)*max_graph_height)
    print(f'{languages[i].rjust(longest_name," ")}: {"#"*percentage} {values[i]}K')




# dictionary implementation
languages={
    "Java":61,
    "Python":47,
    "JavaScript":37,
    "C++":32,
    "C#":26,
    "Ruby":18,
    "Perl":14,
    "PHP":14,
    "C":9,
    "Android":7
}


max_value=max(*languages.values())
longest_name=len(max(*languages.keys(),key=len))
max_graph_height=40 # arbitrary


print("---Dictionary---")

for lang in languages:
    percentage=int((languages[lang]/max_value)*max_graph_height)
    print(f'{lang.rjust(longest_name," ")}: {"#"*percentage} {languages[lang]}K')