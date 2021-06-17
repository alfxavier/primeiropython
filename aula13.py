# Desenvolva um algoritimo que:
# a) leia 4 (quatro) números:
# b) Calcule o quadrado de cada um:
# c) Se o valor resultante do quadrado do terceiro for >= 1000, imprimir e finalize;
# d) caso contrário, imprima os valores lidos e seus respectivos quadrados.

num1 = int(input("informe o primeiro número: "))
num2 = int(input("informe o segundo número: "))
num3 = int(input("informe o terceiro número: "))
num4 = int(input("informe o quarto número: "))

quad1 = num1 ** 2
quad2 = num2 ** 2
quad3 = num3 ** 2
quad4 = num4 ** 2

if quad3 >= 1000:
    print("O quadrado do terceiro é {0}, portanto maior que 1000!".format(quad3))
else:
    print("O quadaro do primeiro é {0}, do segundo é {1}, do terceiro é {2} e do quarto é {3}".format(quad1, quad2, quad3, quad4))
