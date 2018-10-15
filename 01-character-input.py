from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age:"))
msg = "Hi " + name + "! You will turn 100 on year " + str(100 - age + date.today().year)
repeat = int(input("Number of times message should repeat: "))
print(repeat * (msg + "\n"))
