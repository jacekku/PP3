import random as r
values=(
    r.randint(1,6),
    r.randint(1,6),
    r.randint(1,6),
)
for v in values:
    print(v)

print(sum(values))