num = int(input("Enter the number"))
if num % 4 == 0:
    print("Number is even and divisble by 4")
elif num % 2 == 0:
    print("Number is event")
else:
    print("Number is odd")

check = int(input("Enter the divisor"))
print(check, " divides ", num) if (num % check == 0) else print(check, " doesn't divides ", num)
