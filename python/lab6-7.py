#1-2
#list, tuples
information = [("name","Dilnaz"),("lastname","Kalieva"),("age",20)]
for i in information:
    print(i)
print(len(information))
print(type(information))
print(type(information[0]))
print(information[2].count(20))
information.insert(1,("firstname","Nurdauletovna"))
for i in information:
    print(i)
information.sort()
for i in information:
    print(i)

#dictionaries
inf_dictionary = {
    "university":"Satbayev",
    "course":4,
    "profession":"computer science"
}
for inf in inf_dictionary:
    print(inf,":", inf_dictionary[inf])
print(len(inf_dictionary))
print(type(inf_dictionary))

inf_dictionary.pop("course")
print(inf_dictionary)

inf_dictionary["course"] = 4
print(inf_dictionary)

x = inf_dictionary.get("university")
print(x)

k = inf_dictionary.keys()
print(k)

#sets
sets = {"NodeJS","React","VueJS","C++","Java"}
sets2= {"NodeJS","React"}
print("Programming language:",sets)
sets.add("Python")
print("Programming language:",sets)
sets.remove("C++")
print("Programming language:",sets)
print(len(sets))
print(sets2.issubset(sets))
print(sets.difference(sets2))
print(sets.union(sets2))
print(sets.intersection(sets2))
print(type(sets))


#3
from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)
        
for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])

#4
ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

#5
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

#6
num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)


#7
states = {}
for i in range(int(input())): 
    states.update([input().split()])  # перечень штатов (словарь)
    
votes = dict.fromkeys(states,())
for i in range(int(input())): 
    s,c = input().split()
    votes[s] = *votes[s],c  # голоса проголосовавших (словарь)

# кандидаты получившие большинство голосов (словарь)
max_votes = {k:max(sorted(v),key=lambda x: v.count(x)) for k,v in votes.items()}
cands = dict.fromkeys(set(sum(votes.values(),())),0)
for k,v in max_votes.items(): 
    # число голосов выборщиков полученные кандидатами (словарь)
    cands[v] += int(states[k]) 

# вывод кандидатов в порядке убывания числа голосов выборщиков
print(*[f'{c} {v}' for c,v in sorted(cands.items(),key=lambda x: -x[1])], sep='\n')
