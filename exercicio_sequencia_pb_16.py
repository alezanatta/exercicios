from math import ceil

area = float(input("Digite a área a ser pintada: "))

litros = area / 3
latas = ceil(litros / 18)
preco = latas * 80

print(f"Será necessário {latas} latas, custando R${preco}")
