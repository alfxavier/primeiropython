""" 
Esse algoritimo recebe a quantidade de horas trabalhadas no mês e o valor recebido por horas trabalhadas
e retorna o valor recebido no mês.
"""

valor_hora = int(input("Qual o valor da hora trabalhada: "))
horas_trabalhadas = int(input("Quantas horas você trabalhou esse mês: "))

salario = valor_hora * horas_trabalhadas

print("Seu sálário é de {0} reais esse mês".format(salario))