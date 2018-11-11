tab=[7,5,[3,6,[2]],7,[1,[2,3,[4]],9,2],4]

def sum_recursive(tab):
    out=0
    for value in tab:
        if(type(value) is list):
            out+=sum_recursive(value)
        else:
            out+=value
    return out



assert sum_recursive(tab) is 55
assert sum_recursive([[[[[[[[[[[[[[[[1]]]]]]]]]]]]]]]]) is 1
assert sum_recursive([1]) is 1
assert sum_recursive([-1,[1,[-1,[1,[-1,[1,[-1,1]]]]]]]) is 0