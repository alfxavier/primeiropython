# A secretaria de Meio Ambinete que controla o ondice de poluição mantém 3 grupos de industria que são altamente poluentes do meio ambiente. O indice de poluição aceitável varia de 0,05 até 0,25. Se o indice cresce para 0,3 as industrias do 1º grupo são intimadas a suspender suas atividades, se o indice crescer para 0,4 as industrias do 1º e 2º grupo são intimadas a suspender suas atividades. se o indice atingis 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um algoritimo que leia o indicie de poluição medido e emita a notificação adequada aos diferentes grupos

num1 = float(input("Informe o índice medido: "))

if num1 >= 0.05 and num1 <= 0.25:
    print("Índice dentro da normalidade!")
elif num1 > 0.25 and num1 <= 0.3:
    print("Empresa do grupo 1 deve ser suspensa, índice acima do permitido para essa faixa.")
elif num1 > 0.3 and num1 <= 0.49:
    print("Empresas dos grupos 1 e 2 deve ser suspensa, índice acima do permitido para essa faixa.")
elif num1 >= 0.5:
    print("Todas as empresas devem ser suspensas, índice acima que o permitido")
else:
    print("valor fora do padrão")
