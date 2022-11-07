""""faca um programa que dado salario de um colaborador e o reakuste segundo o seguinte criterio, baseado no salario atual
a) Salários até R$ 1280,00 (incluindo) : aumento de 20%
b) Salários entre R$ 1280,00 e R$ 1700,00 : aumento de 15%
c) Salários entre R$ 1700,00 e R$ 2500,00 : aumento de 10%
d) Salários de R$ 2500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:

a) O salário antes do reajuste;
b) O percentual de aumento aplicado;
c) O valor do aumento;
d) O novo salário, após o aumento."""

salario = float(input("informe o salario: "))


if salario <= 1280:
    percentual = 20
elif salario <= 1700:
    percentual = 15
elif salario <= 2500:
    percentual = 10
else:
    percentual = 5

aumento = salario * percentual / 100

novosalario = salario + aumento 

print("salario antigo = ", salario)
print("percentual de aumento = ", percentual)
print("valor de aumento = ", aumento)
print("novosalario = ", novosalario)

