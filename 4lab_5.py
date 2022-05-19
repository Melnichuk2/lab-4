
#Дано текст. Замінити всі входження найбільшої цифри її словесним написанням.

import string
s=str(input("Введите строку:"))
print("Исходная строка:",s)
massiv_cifr =[0]*len(s)
for i in range(len(s)):
    if s[i].isdigit():
      massiv_cifr.append(int(s[i]))
max_cifra = max(massiv_cifr)
lst = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть' , 'семь', 'восемь', 'девять']
max_cifra_opisanie = lst[max_cifra]
subStrOld = str(max_cifra)
subStrNew =max_cifra_opisanie
lenStrOld = len(subStrOld)
while s.find(subStrOld) > 0:
   i = s.find(subStrOld)
   s = s[:i] + subStrNew + s[i+lenStrOld:]
print("Выходная строка:", s)


