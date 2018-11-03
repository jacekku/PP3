def int_input():
    count=""
    while(type(count) is not int):
        try:
            print("Enter an integer")
            count=int(input())
        except ValueError:
            print("Please enter an integer")
    return count



print("Hello World\nEnter your name:")
a=input()
print("Your name is "+a)
count=int_input()
print("Now im going to count to {0} and print the squares also".format(count))

for i in range(count+1):
    print("{0} : {1}".format(i,i*i))
