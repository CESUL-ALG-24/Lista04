numero = int(input("Informe um número inteiro: "))

centena = numero // 100

temp = numero % 100
dezena = temp // 10
unidade = temp % 10

soma = centena + dezena + unidade

print("A soma dos 3 números é", soma)