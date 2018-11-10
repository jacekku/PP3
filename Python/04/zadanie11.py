from snippets import create_matrix,print_matrix
from random import randint


def remove_row_col(matrix,row,col):
    size=len(matrix)
    temp=create_matrix(size-1,size-1)
    temp_x,temp_y=0,0
    for i in range(size):
        for j in range(size):
            if(i==row or j==col):
                pass
            else:
                temp[temp_y][temp_x]=matrix[i][j]
                temp_x+=1
                if(temp_x==(size-1)):
                    temp_x=0
                    temp_y+=1
                
    return temp




def cofactor(i,j,val,matrix):
    #                      two function recursion
    return ((-1)**(i+j))*val*determinant(matrix)

def determinant(matrix):
    if(len(matrix)!=len(matrix[0])):
        raise IndexError("Matrix must be square")
    size=len(matrix)
    if(size==1):
        return matrix[0][0]
    if(size==2):
        return matrix[0][0]*matrix[1][1] - (matrix[0][1]*matrix[1][0])
    det=0
    for j in range(size):
        det+=cofactor(  0,
                        j,
                        matrix[0][j],
                        remove_row_col(matrix,0,j))
    return det

tab=create_matrix(3,3,key=randint,key_args=[0,9])
print_matrix(tab,format="wolfram")
print()
print(determinant(tab))





