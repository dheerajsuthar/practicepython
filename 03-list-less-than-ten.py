a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
filter = int(input("Enter limit"))
b = [i for i in a if i < filter]
print(b)
