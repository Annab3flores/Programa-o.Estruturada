"""
Questão 1

Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para
 desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um
colaborador e o reajuste segundo a tabela a seguir, baseado no salário atual. Após o aumento ser realizado, informe na tela:

O salário antes do reajuste;
O percentual de aumento aplicado;
O valor do aumento;
O novo salário, após o aumento.
"""

def reajuste_salario (salario):

    aumento20 = (salario * 20)/100
    aumento15 = (salario * 15)/100
    aumento10 = (salario *10)/100
    aumento5 = (salario * 5)/100
    
    if salario <= 280:
        return salario + aumento20
    elif salario <= 700:
        return salario + aumento15
    elif salario <= 1500:
        return salario + aumento10
    else:
        return salario + aumento5
    
salario = float(input("Digite o seu salario: "))
salario_novo = reajuste_salario(salario)
print(f"o salario {salario} mudou para {salario_novo}")

"""
Questão 2

Implementa uma função que receba um número e exiba o dia correspondente da semana 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido
"""

def dia_da_semana(num):
    if num == 1:
        return "domingo"
    elif num == 2:
        return "segunda-feira"
    elif num == 3:
        return "terça-feira"
    elif num == 4:
        return "quarta-feira"
    elif num == 5:
        return "quinta-feira"
    elif num == 6:
        return "sexta-feira"
    elif num == 7:
        return "sabado"
    else:
        return "valor inválido"
    
num = int(input("Digite um número de 1 a 7: "))

resultado = dia_da_semana(num)
print(resultado)

"""
Questão 3
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax^2 + bx + c. O programa deverá receber os valores de a, b e c
e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.
"""

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau. Encerrando o programa.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais. Encerrando o programa.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui uma única raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + delta ** 0.5) / (2 * a)
        raiz2 = (-b - delta ** 0.5) / (2 * a)
        print(f"A equação possui duas raízes reais:")
        print(f"Raiz 1: {raiz1:.2f}")
        print(f"Raiz 2: {raiz2:.2f}")