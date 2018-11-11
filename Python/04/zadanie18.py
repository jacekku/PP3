def sum_digits(number):
    if(number<0):
        return sum_digits(-number)
    if(number<10):
        return number
    return number%10 + sum_digits(number//10)


assert sum_digits(1111) is 4
assert sum_digits(1234) is 10
assert sum_digits(-1111) is 4
assert sum_digits(-1234) is 10
assert sum_digits(-100100) is 2
assert sum_digits(9911) is 20
assert sum_digits(-1111) is 4
