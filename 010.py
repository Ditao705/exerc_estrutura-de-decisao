"""10.Faça um Programa que pergunte em que turno você estuda.

Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso."""

t1 = input("informe seu turno: ")

if t1 == "m":
    print("bom dia!")
elif t1 == "v":
    print("boa tarde!")
elif t1 == "n":
    print("boa noite!") 
else:
    print("valor invalido!")
