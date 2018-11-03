fibb=[0,1,None]
for i in range(50):
    print("{0}:{1}".format(i,fibb[0]))
    fibb[2]=sum(fibb[0:2])
    [fibb[0],fibb[1],fibb[2]]=[fibb[1],fibb[2],None]