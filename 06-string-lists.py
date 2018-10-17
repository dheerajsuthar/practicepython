string = input('String: ').lower().replace(' ', '')
l = len(string)
isP = True
for i in range(0, l//2):
    if string[i] != string[l-i-1]:
        isP = False
print(string, " is Pallindrome.") if isP else print(
    string, " is not Pallindrome")
# or
print(string, " is Pallindrome.") if string == string[::-1] else print(
    string, " is not Pallindrome")
