class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def likes(self):
        return self.__likes
    
    def dar_likes(self):
        self._likes += 1

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self._likes} Likes')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super()._init__(nome, ano)

        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

    @property  
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome (self, novo_nome):
        self.__nome =  novo_nome.title() 
        
    @property    
    def nome(self):
        return self.dar__likes
    
    def dar__likes(self):
        self._likes += 1
        
class Serie:
    def __init__(self, nome, ano,temporadas):
        super().__init__(nome,ano)
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0  
        
    def dar__likes(self): 
        self.likes += 1
        
vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime()
