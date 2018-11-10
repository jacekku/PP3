from snippets import create_matrix,print_matrix
from random import randint

def get_row(matrix,row):
    return [matrix[row][i] for i in range(len(matrix[0]))]

def get_col(matrix,col):
    return [matrix[i][col] for i in range(len(matrix))]

mat1=create_matrix(2,2,key=randint,key_args=[0,9])
print_matrix(mat1)
print()
mat2=create_matrix(2,2,key=randint,key_args=[0,9])
print_matrix(mat2)
print()


def dot_product(vector1,vector2):
    size=len(vector1)
    if(size!=len(vector2)):
        raise IndexError("Vectors must be the same size")
    product=0
    for i in range(size):
        product += vector1[i]*vector2[i]
    return product

def matrix_product(mat1,mat2):
    y_size1=len(mat1[0])
    x_size2=len(mat2)
    if(y_size1!=x_size2):
        raise IndexError("Matricies have wrong dimensions")
    product_y_size=len(mat2[0])
    product_x_size=len(mat1)
    product=create_matrix(product_y_size,product_x_size)
    for i in range(product_y_size):
        for j in range(product_x_size):
            product[i][j]=dot_product(get_row(mat1,i),get_col(mat2,j))
    return product


print_matrix(matrix_product(mat1,mat2))