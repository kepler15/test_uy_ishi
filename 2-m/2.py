'''



2-masala. ELECTION
Foydalanuvchi tomonidan Dictionaryga keyga ismlar va valuega esa Boolean type (1 yoki 0) kiritadi. Sizning vazifangiz eng ko'p ovoz berganlarning ismlarini chiqarish. Agar durang bo'lsa, ikkalisini ham chiqarish kerak. Chiqishda birinchi qatorda qaysi qiymat ko'p ovoz berilganini va keying qatorda esa ismlarni chiqarish kerak. Ma'lumotlar chiqishini ma'nunada keltirilgandek bo'lishi kerak.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Input (Kiruvi ma'lumot)	Output (Chiquvchi ma'lumot)
{'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}	1 \n Anvar Lobar Vali Baxtiyor
{'Anvar': 0, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}	0 \n Lobar Vali Baxtiyor
{'Anvar': 0, 'Lobar': 0, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}	0 \n Vali Baxtiyor
{'Anvar': 0, 'Lobar': 0, 'Asror': 0, 'Vali': 0, 'Surayyo': 1, 'Baxtiyor': 0}	0 \n Asror Surayyo


'''


dct = {}

while True:
    soz = input("Ism va raqamni joy tashlab kiritng tugatish uchun 'a' kiriting: ")
    if soz == 'a':
        break
    soz = soz.split(" ")
    if len(soz) == 2 and soz[1].isdigit():
        dct[soz[0]] = int(soz[1])
print(dct)

sanoq = 0
count_val = 0
for i , val in dct.items():
    if val == 1:
        sanoq += 1
    elif val == 0:
        count_val += 1



if count_val > sanoq:
    print('0')
    for i , val in dct.items():
        if val == 0:
            print(i, end = ' ')
    
elif count_val < sanoq:
    print('1')
    for i , val in dct.items():
        if val == 1:
            print(i, end = ' ')    
            
else:
     for i , val in dct.items():
        print('0')
        if val == 0:
            print(i, end = ' ')
     for i , val in dct.items():
        print('1')
        if val == 1:
            print(i, end = ' ')


