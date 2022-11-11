"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""


i = int(input("digite um numero: "))


if i == 1:
    print("domingo")
elif i == 2:
    print("segunda-feira")
elif i == 3:
    print("terça-feira")
elif i == 4:
    print("quarta-feira")
elif i == 5:
    print("quinta-feira")
elif i == 6:
    print("sexta-feira")
elif i == 7:
    print("sábado")
else:
    print("valor invalido")
