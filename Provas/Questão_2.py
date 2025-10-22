#2 - Suponha que estamos desenvolvendo um sistema para um banco. Este sistema deve obedecer as seguintes restrições:
#A - Uma classe pai chamada Cliente, com os atributos: nome, cpf, endereço.

#B - Uma classe filha chamada Conta_Corrente que deve herdar os atributos da classe pai 
#mais o atributo "saldo". Este atributo deve ser privado.

#C - O sistema precisa ser capaz de: depositar, sacar, consultar saldo, consultar informações 
#dos clientes e alterar informações dos clientes. Não deve ser possível ter saldo negativo, 
#nem sacar além do saldo.
#Crie ao menos 1 instância de Conta_Corrente, execute todos os métodos para teste.

class Cliente: #criando a classe pai
    def __init__(self, nome, cpf, endereco): #inicializando o objeto singular cliente, com os parâmetros exigidos
        self.nome=nome
        self.cpf=cpf
        self.endereco=endereco

    def consulta_dados(self):
        return self.nome, self.cpf, self.endereco

    def altera_nome(self, nome):
        self.nome=nome
        return print("Nome alterado com sucesso")
    
    def altera_cpf(self, cpf):
        self.cpf=cpf
        return print("CPF alterado com sucesso")
    
    def altera_endereco(self, endereco):
        self.endereco=endereco
        return print("Endereço alterado com sucesso")
    
class Conta_corrente(Cliente): #criando a classe conta-corrente (filha), criando a condição de herança 
    #com a classe Cliente (pai).
    def __init__(self, nome, cpf, endereco, saldo): #inicializando o objento singular conta-corrente, com os parâmetros
#exigidos. São os mesmos da classe pai, mais o seu próprio
        super().__init__(nome, cpf, endereco)
        self.__saldo=saldo #Como CC herdará os atributos de Cliente, só preciso declarar o atributo
        #próprio da classe. Ou seja, o atributo "saldo". Como este atributo precisa ser "privado",
        #preciso usar o 2 underscores "__" .

    def depositar(self, valor): #criando um método para depositar dinheiro na conta.
        if valor<0: #criando uma condicional, pois não é possível depositar um valor negativo.
            print(f"Valor inválido.")
        else:
            self.__saldo=self.__saldo+valor #atualizando o conteúdo do atributo saldo após o despósito.
    
    def sacar(self, valor): #criando um método para sacar dinheiro da conta.
        if valor<0: #criando uma condicional, pois não é possível sacar um valor negativo.
            print(f"Valor incorreto.")
        elif valor>self.__saldo:
            print(f"Saldo insuficiente.") #criando uma condicional, pois não é possível sacar um valor maior que o saldo.
        else:
            self.__saldo=self.__saldo-valor #atualizando o conteúdo do atributo saldo após o saque.
    
    def consulta_saldo(self):
        print(f"O seu saldo é de R${self.__saldo}")

primeiro_cliente=Conta_corrente(nome="Epaminondas Abreu", cpf="100.002.122-45", endereco="Rua dos Floricultores, nº 21 - Guaratiba",saldo=1000)

print(primeiro_cliente.consulta_dados())
