'''
1-masala. NEIGHBORS
Foydalanuvchi tomonidan Listda faqat butun sonlardan iborat List kiritilgan. Sizning vazifangiz ushbu Listda qo'shni bir xil ishorali elementlarni chiqarish. Agar qo'shni elementlarning ishoralari bir biridan farqli bo'lsa, sonlar chiqarilmasin. Har bir masala shartiga mos qo'shni elementlarni alohida qatorda chiqarilsin.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Input (Kiruvi ma'lumot)	Output (Chiquvchi ma'lumot)
[-1, 2, 3, -1, -2]	
2 3 
 -1 -2
[-1, 2, 3, -1, -4, 5, 6, 7]	
2 3 
 -1 -4 
  5 6 
   6 7




'''

'''
kiritilgan sonlar ichida ishorasi bir xil bolgan qoshni sonlarni chiqarish
'''

son = input("son joy tashlab kiriting:")
lst = son.split(" ")
lst = [int(x) for x in lst]
print(lst)

for i in range(len(lst) - 1):
    if (lst[i] > 0 and lst[i + 1] > 0) or (lst[i + 1] < 0 and lst[i] < 0):
        print(lst[i], lst[i + 1])
    