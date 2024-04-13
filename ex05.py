valor_compra = int(input("Informe o valor da compra: "))
valor_recebido = int(input("Informe o valor recebido: "))

troco = valor_recebido - valor_compra

notas_cem = troco // 100

temp = troco % 100
notas_dez = temp // 10
notas_um = temp % 10

print("Troco")
print(notas_cem, "notas de R$ 100")
print(notas_dez, "notas de R$ 10")
print(notas_um, "notas de R$ 1")