#5
D = {1:'a', 3:4, 'f':3, 'g':'y', 9:4 }
print ('Сумма ключей: ')
sumU=int(0)
for i in D.keys():
     if isinstance (i, int):
         sumU+=int(i)
print (sumU)
print ('Сумма значений: ')
sumF = 0
for i in D.values():
     if isinstance (i, int):
         sumF+=int(i)
print (sumF)

#6
sp1 = [2, 9, 4.1, 6]
sp1.sort()
sp2=[(sp1[i], sp1[j])
     for i in range (len(sp1)-1)
     for j in range(i+1, len(sp1))]
print(sp2)


#7
value = [i for i in sp1 if sp1.index(i)%2 != 0]
key = [i for i in sp1 if sp1.index(i)%2 == 0]
slov = {k:v for k, v in zip(key, value)}
print(slov)
