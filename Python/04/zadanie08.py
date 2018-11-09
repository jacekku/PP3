#the exercise wants me to create a transposition for square maticies but the next one wants me to 
#create one for any size matrix so im going to do it here
from random import randint
def create_matrix(y_size,x_size,key=0,key_args=[]):
    return[
        [
            (key(*key_args) if callable(key) else key) for _ in range(x_size)
        ] for _ in range(y_size)
    ]
    


def transpose_matrix(matrix):
    y_size=len(matrix)
    x_size=len(matrix[0])
    temp=create_matrix(y_size,x_size)
    for i in range(y_size):
        for j in range(x_size):
            temp[j][i]=matrix[i][j]

    return temp
matrix=create_matrix(3,3,key=randint,key_args=[0,9])


print(*matrix,sep="\n",end="\n\n")
print(*transpose_matrix(matrix),sep="\n")
