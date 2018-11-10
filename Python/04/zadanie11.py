from snippets import print_matrix,determinant

P1=(1,1)
P2=(2,2)
P3=(3,3)

matrix=[
    [*P1,1],
    [*P2,1],
    [*P3,1],
]

print_matrix(matrix)
print(determinant(matrix))


P1=(1,1)
P2=(2,2)
P3=(3,1)

matrix=[
    [*P1,1],
    [*P2,1],
    [*P3,1],
]

print_matrix(matrix)
print(determinant(matrix))