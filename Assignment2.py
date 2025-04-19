#Task 1
Input_1 = int(input("Enter a number:"))
if (Input_1%2==1):
    print(f"{Input_1} is a odd number")
else:
    print(f"{Input_1} is a even number")

#Task 2
sum=0
for i in range(1,50,1):
    sum=sum+i
print(f"The sum of numbers from 1 to 50 is: {sum}")