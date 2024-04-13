clientes_isentos = int(input("Informe o número de clientes isentos de pendência: "))
clientes_em_dia = int(input("Informe o número de clientes em dia com as parcelas: "))
clientes_atraso = int(input("Informe o número de clientes com parcelas atrasadas: "))

total = clientes_atraso + clientes_isentos + clientes_em_dia

pc_isentos = clientes_isentos / total * 100
pc_em_dia = clientes_em_dia / total * 100
pc_atraso = clientes_atraso / total * 100

print(pc_isentos, "% dos clientes estão isentos de pendência")
print(pc_em_dia, "% dos clientes estão com as parcelas em dia")
print(pc_atraso, "% dos clientes estão com parcelas em atraso")