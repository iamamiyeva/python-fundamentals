number = int(input("Enter the number: "))

if number <= 0:
    print("Please enter positive number!")
else:
    first=0
    second=1
    fib=[]
    for _ in range(number):
        fib.append(first)
        third = first +second
        first = second
        second = third
print(f"{fib}")
        
