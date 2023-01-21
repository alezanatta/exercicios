
vogais = ["a", "e", "i", "o", "u"]

letra = input("Digite uma letra: ").lower()

if letra in vogais:
    print("É vogal")
else:
    print("É consoante")