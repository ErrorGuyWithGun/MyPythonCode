import time
n = int(input())
x = ""
for i in range(1, n + 1):
    x = x + str(i)
    print(' '*(n-i) + x + x[-2::-1])

for i in range(n-1, 0, -1):
    print(' '*(n-i), sep='', end='')
    for k in range(1, i + 1):
        print(k, end='')
    for k in range(k-1, 0, -1):
        print(k, end='')
    print()
time.sleep(5.5)
