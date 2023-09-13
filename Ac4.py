"""
Exercício 1
"""

def e_primo(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(e_primo(11))
print(e_primo(12))


"""
Exercício 2
"""

def calcular_parcelas(valor_divida):
  parcelas = {}
  parcelas[1] = {

      "valor_juros": 0,
      "valor_total": valor_divida,
      "valor_parcela": valor_divida,
  }
  
  for num_parcelas in [3, 6, 9, 12]:
    
    valor_juros = valor_divida * (num_parcelas / 100)
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / num_parcelas
    parcelas[num_parcelas] = {
      
        "valor_juros": valor_juros,
        "valor_total": valor_total,
        "valor_parcela": valor_parcela,
    }
  
  return parcelas

valor_divida = float(input("Digite o valor da dívida: "))
parcelas = calcular_parcelas(valor_divida)

print("Opções de parcelamento:")
for num_parcelas, parcela in parcelas.items():
  print(f"{num_parcelas} parcelas:")
  print(f"   Valor dos juros: R$ {parcela['valor_juros']:.2f}")
  print(f"   Valor total: R$ {parcela['valor_total']:.2f}")
  print(f"   Valor da parcela: R$ {parcela['valor_parcela']:.2f}")

"""
Exercício 3
"""

intervalo_1 = 0
intervalo_2 = 0 
intervalo_3 = 0
intervalo_4 = 0

while True:
    numero = int(input("Digite um número positivo: "))
    if numero < 0:
        break
    elif numero >= 0 and numero <= 25:
        intervalo_1 += 1
    elif numero >= 26 and numero <= 50:
        intervalo_2 += 1
    elif numero >= 51 and numero <= 75:
        intervalo_3 += 1
    elif numero >= 76 and numero <= 100:
        intervalo_4 += 1

print("Intervalo 1 (0-25):", intervalo_1)
print("Intervalo 2 (26-50):", intervalo_2)
print("Intervalo 3 (51-75):", intervalo_3)
print("Intervalo 4 (76-100):", intervalo_4)
