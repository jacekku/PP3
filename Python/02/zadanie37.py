height=float(input("How tall are you in meters? "))
if(height>5):
    print("Seems like you enter a value in centimeters; converting to meters : {0}cm -> {1}m".format(height,height/100))
    height/=100
weight=int(input("How much do you weight in kilograms? "))
BMI=weight/(height**2)
values={
    15:"very severely underweight",
    16:"severely underweight",
    18.5:"underweight",
    25:"normal (healthy weight)",
    30:"overweight",
    35:"moderately obese",
    40:"severely obese",
    1000:"very severely obese"
}
for v in values:
    if(BMI<v):
        BMI_verdict=values[v]
        break
print("Your BMI is: {0} you are {1}".format(BMI,BMI_verdict))