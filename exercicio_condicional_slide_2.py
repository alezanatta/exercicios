
salario = float(input("Digite o salário: "))

percentual = None

if salario > 0 and salario <= 1280.00:
    percentual = 0.2
elif salario > 1280 and salario <= 1700:
    percentual = 0.15
elif salario > 1700 and salario <= 2500:
    percentual = 0.10
elif salario > 2500:
    percentual = 0.05
else:
    print("Errou!")

if percentual:
    aumento = salario * percentual
    novo_salario = salario + aumento

    print(f"O salário inicial é {salario}")
    print(f"Percentual de aumento aplicado é {percentual*100}%")
    print(f"O aumento será {aumento}")
    print(f"O novo salario será {novo_salario}")