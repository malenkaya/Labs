#1
class Student:
    def __init__(self):
        self.fio = ""
        self.cls = ""
    def __init__(self, fio):
        self.fio = fio
        self.cls = ""
    def __init__(self, fio, cls):
        self.fio = fio
        self.cls = cls
    def __str__(self):
        return "ФИО: "+ self.fio +" Класс: "+ self.cls
#Пустой список учащихся, который будет наполняться
studentList = []
#Форма для пользователя с инструкциями запросов
while True:
    print("+ - Добавить учащегося\nl - Вывести список учащихся\ns - Вывести отсортированный список учащихся\nq -Выход")
    cmd = input()
#Обработка команд
    if cmd == "+":
        print("ФИО:")
        fio = input()
        print("Класс")
        cls = input()
        st = Student(fio, cls)
        studentList.append(st)
#Вывод списка без сортировки
    elif cmd == "l":
        print("------Список учащихся------")
        for student in studentList:
            print(student)
        print("------")
#Вывод сортированного списка
    elif cmd == "s":
        sortedList = studentList
        sortedList.sort(key = lambda x: x.cls)
        print("------Список учащихся------")
        for student in sortedList:
            print(student)
        print("------")
    elif cmd == "q":
        break

#2
groupmates = [
  {
    "name": "StudentOne",
    "group": "111",
    "age": 21,
    "marks": [4, 3, 5, 5, 4]
  },
  {
    "name": "StudenTwo",
    "group": "111",
    "age": 22,
    "marks": [3, 2, 3, 4, 3]
  },
  {
    "name": "StudentThree",
    "group": "111",
    "age": 23,
    "marks": [3, 5, 4, 3, 5]
  },
  {
    "name": "StudentFour",
    "group": "111",
    "age": 24,
    "marks": [5, 5, 5, 4, 5]
  }
]

def print_students(students):
  string = str(input())
  for student in students:
      if student["name"] == string:
          print(student["marks"])
    

print_students(groupmates)

#3
try:
    numbers = []
    print("Введите число")
    num = int(input())
    if num == '':
        num = int(input())
        numbers.append(num)
    else:
        numbers.append(num)
    while num!=0:
        print("Введите число")
        num = int(input())
        numbers.append(num)
except:
    numbers = []
    print("Введите число")
    num = int(input())
    if num == '':
        num = int(input())
        numbers.append(num)
    else:
        numbers.append(num)
    while num!=0:
        print("Введите число")
        num = int(input())
        numbers.append(num)
numbers.sort()
numbers.remove(0)
print("Список чисел в порядке возрастания:")
for item in numbers:
    print(item)

#4
try:
    numbers = []
    print("Введите число")
    num = int(input())
    if num == '':
        num = int(input())
        numbers.append(num)
    else:
        numbers.append(num)
    while num!=0:
        print("Введите число")
        num = int(input())
        numbers.append(num)
except:
    numbers = []
    print("Введите число")
    num = int(input())
    if num == '':
        num = int(input())
        numbers.append(num)
    else:
        numbers.append(num)
    while num!=0:
        print("Введите число")
        num = int(input())
        numbers.append(num)
numbers.sort(reverse = True)
numbers.remove(0)
print("Список чисел в порядке возрастания:")
for item in numbers:
    print(item)

#5
from random import shuffle
 
arr = [*range(1, 50)]
shuffle(arr)
print(sorted(arr[:6]))

#6
def is_sorted(lst):
    if lst == sorted(lst):
        return True
    elif lst == sorted(lst, reverse=True):
        return False
 
print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))