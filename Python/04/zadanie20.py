import os

for i in os.walk("."):
    print("--------------------")
    print("DIR:",i[0])
    print("DIRECTORIES:",*i[1],sep="\n    <DIR>   ")
    print("FILES:",*i[2],sep="\n    ")
