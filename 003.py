"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""


a1 = input("informe a inicial do seu gênero: ")

if a1 == "f":
    print("feminino")
elif a1 == "m":
    print("masculino")
else:
    print("sexo invalido")
