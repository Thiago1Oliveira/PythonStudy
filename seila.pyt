import math

valor1 = int(input())
convite1 = int(input())

quantidade = math.ceil(valor1 / convite1)
quantidade_vendidos = math.ceil(quantidade * 1.23)

quantidade_int = int(quantidade)
quantidade_vendidos_int = int(quantidade_vendidos)

print(quantidade_int)
print(quantidade_vendidos_int)










