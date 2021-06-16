"""
Recebe um núméro e informa se é par ou impar
"""

num1 = int(input("Infomr um número inteiro: "))
p = 0
i = 0

if num1 % 2 == 0:
    p = num1
    print("{0} é par!".format(p)) 
else:
    i = num1
    print("{0} é impar!".format(i)) 

   