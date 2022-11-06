"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""


p1 = float(input("informe o preço do produto: "))

p2 = float(input("informe o preço do produto: "))

p3 = float(input("informe o preço do produto: "))

if p1 < p2 and p3:
    print((p1))
elif p2 < p1 and p3:
    print(p2)
elif p3 < p1 and p2:
    print(p3)
