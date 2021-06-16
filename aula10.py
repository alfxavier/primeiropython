"""
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algorítimo que calcule 
seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7 * altura) - 58
Para mulheres: (62.1 * altura) - 44.7
"""
sexo = input("informe seu sexo. M ou m para mulher e H ou h para homem:")
altura = float(input("Informe sua altura em m. Ex. 1.76: "))

if sexo.lower() == "m":
    peso_ideal = (62.1 * altura) - 44.7
    
elif sexo.lower() == "h":
    peso_ideal = (72.7 * altura) - 58
    
else:
    print("Seu dados estão incorretos.")    
print("Seu peso ideal é de {0}".format(peso_ideal))

