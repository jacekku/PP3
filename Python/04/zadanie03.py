def lists_equal(list1,list2):
    if(len(list1)!=len(list2)):
        return False
    equal=True
    l=len(list1)
    index=0
    while(equal and index<l):
        equal=list1[index]==list2[index]
        index+=1
    return equal

assert lists_equal( [1]         ,[1])           is True
assert lists_equal( []          ,[])            is True
assert lists_equal( [[1]]       ,[[1]])         is True
assert lists_equal( ["ASDF",1]  ,["ASDF",1])    is True
assert lists_equal( [1,2]       ,[1])           is False
assert lists_equal( []          ,[1])           is False
print("ALL TESTS PASSED")