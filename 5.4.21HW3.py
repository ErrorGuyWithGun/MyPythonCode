numb = '0123456789'
ModeS = ''
fl = 0
s = str(input("Введите строку: "))
for x in range(len(s)):
    for i in range(len(numb)-1):
        if s[x]==numb[i]:
            fl += 1
    if fl==1:
        ModeS = ModeS+s[x]+' '
        fl = 0
    else:
        ModeS = ModeS+s[x]
print (ModeS.replace(" )", ")"))
