"""Faça um Programa que leia três números e mostre-os em ordem decrescente"""

n1 = int(input("n:"))

n2 = int(input("n:"))

n3 = int(input("n:"))


if n1 >= n2 and n1 >= n3:
    print(n1)
    if n2 >= n3:
        print(n2)
        print(n3)
    else:   
        print(n2)
        print(n3)
elif n2 >= n3:
    print(n2)
    if n1 >= n3:
        print(n1)
        print(n3)
    else:   
        print(n3)
        print(n1)
else:
    print(n3)
    print(n2)
    if n1 >= n2:
        print(n1)
        print(n2)
    else:   
        print(n2)
        print(n1)
