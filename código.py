import random

print("Bem vindo(a) ao quebrador de senhas")

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&?,.;:/\|][{}-+="

numerodesenhas = input("Diga a quantidade de senhas que vai usar: ")
numerodesenhas = int(numerodesenhas)

tamanho = input("Digite o tamanho da senha: ")
tamanho = int(tamanho)

print("\n Aqui estão suas senhas,boa sorte: ")

for pwd in range(numerodesenhas):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(caracteres)
    print(senhas)

