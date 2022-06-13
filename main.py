string1 = "   This is a string.  a   s"
string2 = "  This is another string."
print(len(string1))
print(string1.title())
print(string1.lower())
print(string1.upper())
print(string1.rstrip())
print(string1.lstrip())
print(string1.strip())
print(string1.strip('s'))

d = "qwerty"
ch = d[2]
chm = d[1:3]
print(chm)
chm = d[1:]
print(chm)
chm = d[:3]
print(chm)
chm = d[:]
print(chm)
chm = d[1:5:2]
print(chm)
# d[2]= 'o'

a = 4
b = 3
print(a / b)
print(a % 2)
print(b ** 10)
# преобразование данных
param = "string" + str(15)
n1 = input("Enter the first number:  ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)
# форматирование строк
a = 1 / 3
print("{:7.3f}".format(a))
a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
# списки
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(list1)

list1.insert(0,3)
print(list1)

list2=[100,200,400]
list1.append(list2)
print(list1)
list1.remove([100,200,400])
print(list1)

print(list1.sort(reverse = True))
list_sorted = sorted(list1)
#кортежи
seq = (2,8,23,97,92,44,17,39,11,12,8)
print(seq, " - кортеж")
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(type(seq))
listseq = list(seq)
print(type(listseq))
#словари
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
D['food']
D['quantity'] += 10

#Вложенность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
 'job': ['dev', 'mgr'],
 'age': 25}

print(rec['name']['firstname'], ' ',rec['name']['lastname'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec)
