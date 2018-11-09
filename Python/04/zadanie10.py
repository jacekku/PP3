from snippets import create_matrix,print_matrix
from random import randint
def sum_matricies(mat1,mat2):
    if(len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0])):
        raise IndexError("Matricies must be the same size")

    y_size=len(mat1)
    x_size=len(mat2)
    temp=create_matrix(y_size,x_size)
    for i in range(y_size):
        for j in range(x_size):
            temp[i][j]=mat1[i][j]+mat2[i][j]

    return temp

mat1=create_matrix(3,3,key=randint,key_args=[0,9])
mat2=create_matrix(3,3,key=randint,key_args=[0,9])

print_matrix(mat1)
print()
print_matrix(mat2)
print()
s=sum_matricies(mat1,mat2)
print_matrix(s)

