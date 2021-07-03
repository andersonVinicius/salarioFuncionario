class Funcionario:
    def __init__(self,id,nome,salario):
        self.id = id
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        print("Impossivel alterar salario diretamente. Use a funcao.")

    def calcula_salario(self,taxa):
        self.__salario= self.__salario + (self.__salario * taxa)
        # self.setSalario( n_sal )

