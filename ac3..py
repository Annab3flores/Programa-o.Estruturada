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
