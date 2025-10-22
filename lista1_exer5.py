# Desenvolva um programa que peça ao usuário para inserir as notas de três provas e calcule a média aritmética dessas notas

#Farei algo diferente. Ao invés de pedir as 3 notas dentro de prints soltos, farei numa estrutura de repetição para "x" notas

#Declaração de variáveis
num_de_provas= int(input("Quantas provas você deseja corrigir? "))
i=0
soma=0

while i <num_de_provas:
    nota=float(input("Digite a nota: "))
    i=i+1
    soma=soma+nota

média_arit=soma/num_de_provas

print("A média aritmética é: ", média_arit)