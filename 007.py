"""Faça um Programa que leia três números e mostre o menor dele"""

n1 = float(input("digite um numero: "))

n2 = float(input("digite um numero: "))

n3 = float(input("digite um numero: "))

if n1 < n2 and n3:
    print(n1)
elif n2 < n1 and n3:
    print(n2)
elif n3 < n1 and n2:
    print(n3)
