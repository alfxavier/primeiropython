# Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou impar, e se é positivo ou negativo.

num1 = int(input("informe um número inteiro positivo ou negativo"))

if num1 % 2 == 0 and num1 > 0:
    print("O numero é par e positivo")
elif num1 % 2 == 0 and num1 < 0:
    print("O número é par e negativo")
elif num1 > 0:
    print("O numero é impar e positivo")
else:
    print("O número é impar e negativo")
    