"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

a1 = input("digite uma letra: ")

vogais = ["a","e","i","o","u"]

if a1 in vogais:
    print("vogal")
else:
    print("consoante")
