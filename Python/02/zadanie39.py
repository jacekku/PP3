def half_adder(A,B):
    A=int(A)
    B=int(B)
    return [A^B,A&B]

def full_adder(A,B,CI):
    A=int(A)
    B=int(B)
    CI=int(CI)
    first=half_adder(A,B)
    second=half_adder(CI,first[0])
    #print(f'{A}+{B} (carry:{CI})={second[0]} carry:{first[1]|second[1]}')
    return [
        second[0],          #sum
        first[1]|second[1]  #carry
    ]

def add_binary(num1:str,num2:str):
    #making the numbers the same length
    fill=max(len(num1),len(num2))+1
    num1=num1.rjust(fill,"0")
    num2=num2.rjust(fill,"0")
    
    _carry=0
    _sum=""
    for i in range(1,len(num1)+1):
        _bit_sum,_carry=full_adder(num1[-i],num2[-i],_carry)
        _sum+=str(_bit_sum)
    _sum=_sum[::-1]
    return str(int(_sum))

n="0"
one="1"

for i in range(16):
    print(f'{n.rjust(4,"0")}')
    n=add_binary(n,one)
