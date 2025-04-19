# Task 1
fact_value=1
def fact(input_1):
    if input_1==1:
        return fact_value
    return input_1*fact(input_1-1)

input_1=int(input("Enter a number: "))
print(f"Factorial of {input_1} is: {fact(input_1)}")

# Task 2
from math import *
def cal(input_1):
    print(f"Square root: {input_1 ** (1 / 2)}")
    print(f"Logarithm:{log(input_1,10)}")
    print(f"Sine:{sin(input_1)}")
cal(int(input("Enter a number: ")))
