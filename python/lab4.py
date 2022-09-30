#1
string = str(input())
upper = 0
lower = 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())

#2
a, b = input(), input()
while not(a.isdigit() and b.isdigit()):
    a, b = input(), input()
print(int(a) + int(b))

#3
s = 'Dilnaz'
print([ord(c) for c in s])