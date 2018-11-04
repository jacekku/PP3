from random import randint

def bubble_sort(arr):
    length=len(arr)
    for i in range(1,length):
        for n in range(0,length-i):
            if(arr[n]>arr[n+1]):
                arr[n],arr[n+1]=arr[n+1],arr[n]
    return arr


tab=[randint(1,100) for _ in range(10)]

print(tab)
print(bubble_sort(tab))