import math

print("===== KALKULATOR =====")
print("+  = Penjumlahan")
print("-  = Pengurangan")
print("*  = Perkalian")
print("/  = Pembagian")
print("%  = Modulus")
print("sin = Sinus")
print("cos = Cosinus")
print("tan = Tangen")
print("akar = Akar Kuadrat")
print("pangkat = Pangkat")
print("kuadrat = Kuadrat")

bil1 = float(input("bil 1 = "))
opr = input("opr = ")

if opr in ["sin", "cos", "tan", "akar", "kuadrat"]:
    if opr == "sin":
        hasil = math.sin(math.radians(bil1))
        print("sin", bil1, "=", hasil)

    elif opr == "cos":
        hasil = math.cos(math.radians(bil1))
        print("cos", bil1, "=", hasil)

    elif opr == "tan":
        hasil = math.tan(math.radians(bil1))
        print("tan", bil1, "=", hasil)

    elif opr == "akar":
        if bil1 >= 0:
            print("√", bil1, "=", math.sqrt(bil1))
        else:
            print("Error: bilangan tidak boleh negatif")

    elif opr == "kuadrat":
        print(bil1, "² =", bil1 ** 2)

elif opr in ["+", "-", "*", "/", "%", "pangkat"]:
    bil2 = float(input("bil 2 = "))

    if opr == "+":
        print(bil1, "+", bil2, "=", bil1 + bil2)

    elif opr == "-":
        print(bil1, "-", bil2, "=", bil1 - bil2)

    elif opr == "*":
        print(bil1, "x", bil2, "=", bil1 * bil2)

    elif opr == "/":
        if bil2 != 0:
            print(bil1, ":", bil2, "=", bil1 / bil2)
        else:
            print("Error: tidak bisa dibagi 0")

    elif opr == "%":
        print(bil1, "%", bil2, "=", bil1 % bil2)

    elif opr == "pangkat":
        print(bil1, "^", bil2, "=", bil1 ** bil2)

else:
    print("Error: Operator tidak tersedia")