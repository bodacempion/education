voz_sobaki = 0
voz_cheloveka2 = 0
PerVtorG = (10.5)
SledG = (4)
voz_cheloveka = int(input())
if voz_cheloveka == 0:
    print("WARNING YOU ARE NOT BORN")

elif voz_cheloveka == 1:
    print(PerVtorG)

elif voz_cheloveka == 2:
    voz_sobaki = voz_cheloveka * PerVtorG
    print(voz_sobaki)
    
else:
    voz_cheloveka2 = voz_cheloveka - 2
    voz_sobaki = voz_cheloveka2 * 4 + 21
    print(voz_sobaki)
