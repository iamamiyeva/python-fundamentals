import math

#using math module

n = int(input("Enter the number to find its factorial: "))
print("Result:", math.factorial(n), "\n")

# second method with for loop

fac=1
num = int(input("Enter the number: "))


for i in range(1, num+1):
    fac*=i

print(f"Factorial of {num} is {fac}\n")


# third method with while loop

number = int(input("Enter a number to find its factorial: "))

i=1
fac=1
while(i<=number):
    fac*=i
    i+=1
print(f"{number}! = {fac}")