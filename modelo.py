class Filme:
    def __init__(self, nome,ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    @property  
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self, novo_nome):
        self.__nome =  novo_nome.title() 
        
    @property    
    def nome(self):
        return self.dar__likes
    
    def dar__likes(self):
        self.likes += 1
        
class Serie:
    def __init__(self, nome, ano,temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0  
        
    def dar__likes(self):
        self.likes += 1
        
vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - duracao: {vingadores.duracao} - likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - temporadas: {atlanta.temporadas} - likes:{atlanta.likes}')
f'- temporadas '