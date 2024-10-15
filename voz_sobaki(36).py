# name=input("Введите имя: ")
# surname=input("Введите фамилию: ")
# year=input("Введите год рождния: ")
# print("Здравствуйте", name, surname, "Ваш возраст", 2024 - int(year))
# print(F"Здравствуйте {name} {surname}. Ваш возраст: {2024 - int(year)}")

# a_1=int(input())
# a_2=int(input())
# a_3=int(input())
# a_4=int(input())
# a_5=int(input())
# print("Ваш средний балл", (a_1 + a_2 + a_3 + a_4 + a_5) /5)
 
voz_sobaki = 0
voz_cheloveka2 = 0
PerVtorG = (10.5)
SledG = (4)
voz_cheloveka = int(input())
if voz_cheloveka == 0:
    print("WARNING YOU ARE NOT BORN")
elif voz_cheloveka == 2:
    voz_sobaki = voz_cheloveka * PerVtorG
    print(voz_sobaki)
else:
    voz_cheloveka2 = voz_cheloveka - 2
    voz_sobaki = voz_cheloveka2 * 4 + 21
    print(voz_sobaki)

"""
1 год считает неправильно

"""