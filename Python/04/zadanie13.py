from snippets import create_matrix,print_matrix,transpose_matrix,copy_matrix,determinant
from random import randint

def insert_row(dest_matrix,source_matrix,index):
    """
    Row insertion
    """
    temp=copy_matrix(dest_matrix)
    temp[index]=[*source_matrix]
    return temp

def insert_col(dest_matrix,source_matrix,index):
    """
    Col insertion
    """
    dest_matrix=transpose_matrix(dest_matrix)
    return transpose_matrix(insert_row(dest_matrix,source_matrix,index))

def cramer(matrix,free):
    W=determinant(matrix)
    W1=determinant(insert_col(matrix,free,0))
    W2=determinant(insert_col(matrix,free,1))
    W3=determinant(insert_col(matrix,free,2))
    if(W!=0):
        x=W1/W
        y=W2/W
        z=W3/W
        return (x,y,z)
    if(W==0):
        if(W1==0 or W2==0 or W3==0):
            return None
        if(W1==0 and W2==0 and W3==0):
            return "INFINITE"
matrix=[
    [2,5,3],
    [4,2,5],
    [3,8,4]
]
free=[
    5,4,9
]
print(cramer(matrix,free))

matrix=[
    [2,8,-1],
    [3,2,5],
    [9,-6,4]
]

free=[
    5,4,1
]
print(cramer(matrix,free))