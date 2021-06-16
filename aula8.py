"""
algarítimo que le um número e se positivo armazena em a se negativo armazena em b. 
E se for zeo informa que é zero.
"""

num1 = int(input("Informe um número: "))

if num1 > 0:
    a = num1
    print("Número Positivo")
if num1 < 0:
    b = num1
    print("Número negativo")
else: 
    print("O número é zero!")