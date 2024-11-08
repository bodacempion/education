
bykv_input = (input("Введите букву ")).lower()
bykv = {
    "a" : "гласная",
    "e" : "гласная",
    "i" : "гласная",
    "o" : "гласная",
    "u" : "гласная"
}
if bykv_input == "y":
    print("буква y может быть гласной так и согласной")
elif bykv_input in bykv:
    print(f"Ваша буква {bykv[bykv_input]}")
else:
    print("Эта буква согласная")