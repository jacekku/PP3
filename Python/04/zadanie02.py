'''
get the longer list
iterate over the range of shorter list length
add the indices of both lists storing them in longer list
return longer list
'''

def get_sum_of_indicies(list_2D,index):
    s=0
    for l in list_2D:
        try:
            s+= (l[index])
        except IndexError as err:
            s+=0
    return s


def sum_lists(*lists):
    longest=max(*lists,key=len)
    temp=[]
    for index in range(len(longest)):
        temp.append(get_sum_of_indicies(lists,index))
    return temp

lists=[
    [1],
    [2,3],
    [4,5,6],
    [7,8,9,10]
]


for l in lists:
    print(l)
print("=")
print(sum_lists(*lists))