"""Elabore um algorotimo que leia as variáveis 'c' e 'n', respectivamente código e número de horas 
trabalhadas de um operário. Calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. 
Quando o número de horas exceder a 50 calcule o excesso de pagamento armazenando-o na variáve 'e' . 
Caso contrário zera tal variável. A hora excedente de trabalho vale R$ 20,00. No final do 
processamento imprimir o salário toral e o salário excedente."""

c = int(input("Informe o código do funcionário: "))
n = float(input("Informe o número de horas trbalhadas: "))

if n > 50:
    e = n - 50
    salario_excedente = e * 20 
    salario_total = salario_excedente + (50 * 10)
    print("Salário total recebido R$ {0:.2f}, total de horas extras R$ {1:.2f}.".format(salario_total, salario_excedente))
else:
    salario_total = n * 10
    print("Salário total recebido foi de R$ {0:.2f}.".format(salario_total)) #{.2f} é para formatar o valar com 2 casas decimais
