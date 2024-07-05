'''
1-masala.

Tasavvur qiling-a, sizda berilgan naqshga muvofiq turli xil ranglar bilan toʻldirishingiz kerak boʻlgan kvadratchalar qatori bor.
 Kvadratchalarni ketma-ket boʻyash kerak, ya’ni keyingi kvadrat boshqa rangda boʻlsa, qalamni oʻzgartirishingiz kerak boʻladi.

Eslatma: Barcha ma’lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qoʻyiladi.

Ranglar roʻyxatini oladigan va butun naqshni toʻldirish uchun zarur boʻlgan vaqtning qiymatini (soniyalarda) qaytaradigan funksiyani yozing. Bunda:
- qalamni almashtirish uchun 1 soniya kerak boʻladi
- kvadratni toʻldirish uchun 2 soniya kerak boʻladi

Input (Kiruvchi ma’lumot)                                 Output (Chi'quvchi ma’lumot)
naqsh(["Red", "Blue", "Red", "Blue", "Red"])                 14
naqsh(["Blue"])                                              2
naqsh(["Red", "Yellow", "Green", "Blue"])                    11
naqsh(["Blue", "Blue", "Blue", "Red", "Red"])                11


'''

rang = input("ranglarni bosh joy tashlab kiriting:")
lst = rang.split(" ")
print(lst)

all_time = 2

for i in range(1,len(lst)):
    if lst[i] != lst[i-1]:
        all_time += 3
    else:
        all_time += 2
print(all_time)

