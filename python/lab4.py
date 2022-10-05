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

#4
print(len('dilnaz'))

#5
S = 'dilnaz'
print(S[0])
print(S[2])
print(S[-2])

#6
s = 'dilnaz'
print(s[1:3])

#7
welcome = "Hello world! Goodbye world!"
index = welcome.find("wor")
print(index)

#8
phone = "+1-234-567-89-10"
edited_phone = phone.replace("-", " ")
print(edited_phone)

#9
word = "hello"
joined_word = "|".join(word)
print(joined_word)

#10
word = "python"
print(word.capitalize())


