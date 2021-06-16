"""Joao da Silva, pescador, comprou um microcomputador para controlar o rendimento diário de seu 
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de 
pesca do estado de SP (50 kg) deve pagar uma multa de R$ 4,00 por kg excedente.
João precisa que você faça uma algoritmo que leia a variável "p" (peso de peixes) e 
verifique se há excesso. Se houver gravar na variável "e" (excesso) e na variável "m" o 
valor da multa que Joao deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo "zero".
"""

p = int(input("Peso pescado no dia em Kg: "))

if p <= 50:
    print("Multa: zero")
else: 
    e = p - 50
    m = e * 4
    print("Você excedeu {0} KG e terá que pagar R$ {1}".format(e, m))