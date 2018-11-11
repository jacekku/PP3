def get_largest_value(matrix):
    largest_value=max(*matrix,key=lambda x:max(*x))
    largest_value=max(*largest_value)
    return largest_value

def format_table(format):
    if(format=="clean"):
        return ("",""," ")
    if(format=="wolfram"):
        return ("{","}",",")

def print_matrix(matrix,format="clean"):
    if(len(matrix)==1):
        print(matrix[0][0])
        return
    longest_value=len(str(get_largest_value(matrix)))

    starting_symbol,end_symbol,separator=format_table(format)
    print(end=starting_symbol)
    for row in matrix:
        print(starting_symbol,end="")
        for val in row:
            print(f'{val:{longest_value}d}',end=separator)
        print(end_symbol+separator)
    print(end=end_symbol)

def create_matrix(y_size,x_size,key=0,key_args=[]):
    return[
        [
            (key(*key_args) if callable(key) else key) for _ in range(x_size)
        ] for _ in range(y_size)
    ]


def copy_matrix(matrix):
    y_size=len(matrix)
    x_size=len(matrix[0])
    temp=create_matrix(y_size,x_size)
    for i in range(y_size):
        for j in range(x_size):
            temp[i][j]=matrix[i][j]
    return temp


def transpose_matrix(matrix):
    y_size=len(matrix)
    x_size=len(matrix[0])
    temp=create_matrix(x_size,y_size)
    for i in range(y_size):
        for j in range(x_size):
            temp[j][i]=matrix[i][j]

    return temp



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
        det+=((-1)**(0+j))*matrix[0][j]*determinant(remove_row_col(matrix,0,j))
    return det


def get_row(matrix,row):
    return [matrix[row][i] for i in range(len(matrix[0]))]

def get_col(matrix,col):
    return [matrix[i][col] for i in range(len(matrix))]

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