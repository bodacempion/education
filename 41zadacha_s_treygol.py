one_ygol = int(input("1 угол:"))
two_ygol = int(input("2 угол:"))
three_ygol = int(input("3 угол:"))
if one_ygol == two_ygol == three_ygol:
    print("треугольник равносторонний")
elif one_ygol == two_ygol >= three_ygol or one_ygol == two_ygol <= three_ygol or one_ygol == three_ygol <= two_ygol or one_ygol == three_ygol >= two_ygol or two_ygol == three_ygol >= one_ygol or two_ygol == three_ygol <= one_ygol:
    print("треугольник равнобедренный")
else:
    print("треугольник разносторонний")