#Crie um programa que solicite ao usuário o preço de três produtos e calcule o valor total da compra.

#Declarando as variáveis

produto_1=float(input("Digite o preço do primeiro item: "))
produto_2=float(input("Digite o preço do segundo item: "))
produto_3=float(input("Digite o preço do terceiro item: "))
preço_total=produto_1+produto_2+produto_3

#Exibindo o preço na tela
print("O total da compra foi de: ", preço_total)