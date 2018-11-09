size=4
matrix=[
    [
        0 for _ in range(size)
    ] for _ in range(size)
]
for i in range(size):
    matrix[i][i]=1

print(*matrix,sep="\n")