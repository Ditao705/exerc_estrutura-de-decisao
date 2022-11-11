"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre 4.0 e zero        E"""


a = float(input("valor da sua nota: "))


if a <= 4.0:
    print("media: E")
elif a <= 6.0:
    print("media: D")
elif a <= 7.5:
    print("media: C")
elif a <= 9.0:
    print("media: B")
elif a <= 10.0:
    print("media: A")
else:
    print("valor invalido")
