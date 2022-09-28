#1
print([k for k in range(int(input("Введите цифру A = :")),int(input("Введите цифру B = :"))+1)])

#2
A = int(input("Введите цифру A = :"))
B = int(input("Введите цифру B = :"))
if A < B :
    for i in range(A,B+1):
        print(i)
else :
    for i in range(B,A+1):
        print(i)

#3
A = int(input("Введите цифру A = :"))
B = int(input("Введите цифру B = :"))
for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i)

#4
N = int(input("Введите количество карточек :"))
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)

#5
import random
 
r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))
 
r2 = random.randint(-10, -1)
print("Random number between -10 and -1 is % d" % (r2))
 
r3 = random.randint(-5, 5)
print("Random number between -5 and 5 is % d" % (r3))