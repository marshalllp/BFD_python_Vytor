#1 - Construa uma classe para armazenar informações de carros, 
# cada objeto instanciado por essa classe deve ter os seguintes atributos:
#A - Modelo, marca, ano de lançamento, potência (1.0,1.6,etc), tipo de câmbio (manual ou automático), 
#preço no lançamento.
#B - Crie um método para retornar cada atributo.
#Crie ao menos 3 instâncias de objeto, e execute todos os métodos para teste.

class Automovel: #criando a classe automovel/ carro
    def __init__(self, modelo, marca, ano, potencia, cambio, preco_lanca): #inicializando o objeto 
        #singular/único automóvel/carro
        self.modelo=modelo #introduzindo os atributos referenciados ao objeto singular/único
        #automovel/carro, que serão entregues pelos parâmetros exigidos pelo método init 
        self.marca=marca
        self.ano=ano
        self.potencia=potencia
        self.cambio=cambio
        self.preco_lanca=preco_lanca
    
    def retorna_mod(self): #criando métodos para retornar os atributos
        return self.modelo #Devo escrever self.modelo ao invés de só "modelo" porque self.modelo é
    #onde está guardado o conteúdo do atributo. Já somente "modelo" é uma variável local/ parâmetro.
    
    def retorna_marca(self):
        return self.marca
    
    def retorna_ano(self):
        return self.ano
    
    def retorna_pot(self):
        return self.potencia
    
    def retorna_cambio(self):
        return self.cambio
    
    def retorna_preco_lanca(self):
        return self.preco_lanca
    
#Criando as instâncias de objetos que deverão conter os parâmetros exigidos pelo método init.
carro1=Automovel(modelo="Corolla", marca="Toyota", ano=2011, potencia=1.8, cambio="Automático", preco_lanca="R$ 180.000")
carro2=Automovel(modelo="Clio", marca="Renault", ano=2011, potencia=1.0, cambio="Manual", preco_lanca="R$ 30.000")
carro3=Automovel(modelo="Impreza", marca="Subaru", ano=2011, potencia=2.0, cambio="Manual", preco_lanca="R$ 75.000")

#Imprimindo o retorno de cada método.
print(f"O carro {carro1.retorna_mod()}, da marca {carro1.retorna_marca()}, do ano de {carro1.retorna_ano()} com motor {carro1.retorna_pot()} e câmbio {carro1.retorna_cambio()} foi lançado ao preço de {carro1.retorna_preco_lanca()}.")
print(f"O carro {carro2.retorna_mod()}, da marca {carro2.retorna_marca()}, do ano de {carro2.retorna_ano()} com motor {carro2.retorna_pot()} e câmbio {carro2.retorna_cambio()} foi lançado ao preço de {carro2.retorna_preco_lanca()}.")
print(f"O carro {carro3.retorna_mod()}, da marca {carro3.retorna_marca()}, do ano de {carro3.retorna_ano()} com motor {carro3.retorna_pot()} e câmbio {carro3.retorna_cambio()} foi lançado ao preço de {carro3.retorna_preco_lanca()}.")

#Eu tinha escrito dessa forma. Porém, não atende à resposta do problema. Caso esteja assim, não estou 
# imprimindo na tela o retorno do método, mas sim  o objeto instanciado:
#print(f"O carro {carro3.modelo}, da marca {carro3.marca}, do ano de {carro3.ano} com motor {carro3.potencia} e câmbio {carro3.cambio} foi lançado ao preço de {carro3.preco_lanca}.")

#Tentei imprimir assim també: print(f"O carro {carro1.retorna_mod}, mas dava o erro de que o programa
#imprimia o espaço de memória alocado. Faltaram os parênteses.