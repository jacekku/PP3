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




