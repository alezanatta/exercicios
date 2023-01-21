
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

while usuario == senha:
    print("Usuário e senha inválidos. Tente novamente. ")

    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

print("Foi!")
