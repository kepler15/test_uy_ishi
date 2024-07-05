"""
6-masala. SORTING

My_sort nomli funksiya yarating va ushbu funksiyaga parameter sifatida faqat butun sonlardan iborat List ma'lumotlari beriladi. Sizning vazifangiz bu funksiyaga qiymat qaytarish sifatida Listning har bir elementlarining raqamlar yig'indisi bo'yicha o'sish tartibida saralash kerak. Foydalanuvchi List elementlariga faqat musbat sonlar kirita oladi va shuni shartini ham exception orqali tekshirib oling.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Input (Kiruvchi ma'lumot)	Output (Chi'quvchi ma'lumot)
My_sort([14, 30, 103])  	[30, 103, 14]
My_sort([5, 31, 123, 80, 11])	[11, 31, 5, 123, 80]


"""


def My_sort(lst):
    a = sorted(lst, key = sum_raqam)
    return a

def sum_raqam(son):
    return sum(int(raqam) for raqam in str(son))




son = int(input("Listga kiritiladigan sonlar sonini kiriting: "))
lst = []
i = 0

while i < son:
    try:
        number = int(input(f"{i + 1} ==> "))
        if number < 0:
            raise ValueError("Musbat son kiriting:")
        lst.append(number)
        i += 1  
    except ValueError as e:
        print(e)
lst_sort = My_sort(lst)
print(lst_sort)
