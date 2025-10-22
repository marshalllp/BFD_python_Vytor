#3 - Suponha que você faz parte de uma equipe de desenvolvimento para softwares de astronomia e 
# irá criar um protótipo expansível de sistema solar, para isso siga as definições:
#A - Crie uma classe Planeta, ela deve ser inicializada com os parâmetros: 
# nome, raio_equatorial, distancia_do_sol e composicao.

#B - O raio_equatorial deve ser em km, a distancia_do_sol em milhões de km e 
# composição "Rochoso" ou "Gasoso".

#C - Adicione um método de apresentação, sem parâmetros, que mostre na tela as informações do planeta.

#D - Fora da classe, crie uma função que calcule e retorne o 
# valor da distância do planeta instanciado até o SOL em UA 
# (Unidades Astronômicas, representada pela distância da terra até o Sol, 
# aproximadamente 150 milhões de km). Utilize a fórmula: distancia_do_sol / 150. 
# Essa função deve receber como parâmetro o atributo distancia_do_sol da classe planeta, ou seja, deve 
# funcionar para qualquer objeto do tipo planeta.

#Pesquisa na internet pelas informações de 3 planetas e as utilize para instanciar 3 objetos. 
# Execute o método de apresentação e a função de distância para cada um dos objetos instanciados.



class Planeta: #criando a classe Planeta
    def __init__(self, nome, raio_equatorial, distancia_do_sol, composicao): #inicializando um objeto individualizado na classe Planeta, com os parâmetros propostos.
        self.raio_equatorial=raio_equatorial #introduzindo os atributos referenciados ao objeto singular/único
        #planeta, que serão entregues pelos parâmetros exigidos pelo método init
        self.distancia_do_sol=distancia_do_sol
        self.composicao=composicao
        self.nome=nome
    
    def exibe_informacoes(self):
        return print(f'O planeta {self.nome} tem raio equatorial de {self.raio_equatorial} km, está a {self.distancia_do_sol} milhões de km do sol e tem composição {self.composicao}.')
    


def calcula_dist(planeta):

    return planeta.distancia_do_sol/150


planeta_Marte=Planeta(nome="Marte", raio_equatorial=3398, distancia_do_sol=227.9,composicao="Rochosa")
planeta_Jupiter=Planeta(nome="Júpiter",raio_equatorial=71492, distancia_do_sol=778.3,composicao="Gasosa")
planeta_Plutao=Planeta(nome="Plutão",raio_equatorial=1188, distancia_do_sol=5913.5,composicao="Rochosa")

print(f'{calcula_dist(planeta_Marte):.2f}')
planeta_Marte.exibe_informacoes()

print(f'{calcula_dist(planeta_Jupiter):.2f}')
planeta_Jupiter.exibe_informacoes()

print(f'{calcula_dist(planeta_Plutao):.2f}')
planeta_Plutao.exibe_informacoes()