#1
L = []
x= []
a = input ('Введите количество элементов списка: ')
for i in range(int(a)): #ввод 
    L.append((input('Введите элемент списка: ' ))) #добавление целого числа, введенного с клавиатуры, в конец списка
for i in L:
    if i  % 2 == 0:
        x.append(i)
print ('Вывод чётных элементов списка: ')
print (x)
x.clear()
#2
for i in range (0,int(a),2):
    if i == 0:
        continue
    x.append(L[i])
print ('Вывод элементов списка с чётным индексом: ')
print (x)
x.clear()
#3
for i in L:
    if i > 0:
        x.append(i)
print ('Вывод положительных элементов списка: ')
print(x)
x.clear()
#4
m = 3 
for i in L:
    if i>=m:
        if i % m == 2:
            print ('Число '+ str(i) +' делиться c остатком в два: ')
        if i % m == 1:
            print ('Число ' + str(i) + ' делиться c остатком в единицу: ')
        if i % m == 0:
            print ('Число ' + str(i) + ' делиться без остатка: ')
