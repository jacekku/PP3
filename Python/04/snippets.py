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
    print(starting_symbol)
    for row in matrix:
        print(starting_symbol,end="")
        for val in row:
            print(f'{val:{longest_value}d}',end=separator)
        print(end_symbol+separator)
    print(end_symbol)

def create_matrix(y_size,x_size,key=0,key_args=[]):
    return[
        [
            (key(*key_args) if callable(key) else key) for _ in range(x_size)
        ] for _ in range(y_size)
    ]
    
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
        #two function recursion
        det+=cofactor(  0,
                        j,
                        matrix[0][j],
                        remove_row_col(matrix,0,j))
    return det


