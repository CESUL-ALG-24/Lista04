largura = float(input("Informe a largura do pacote: "))
altura = float(input("Informe a altura do pacote: "))
comprimento = float(input("Informe o comprimento do pacote: "))

qtde_barbante = (largura * 2) + (altura * 4) + (comprimento * 2) + 20

print("Serão necessários", qtde_barbante, "cm de barbante")
