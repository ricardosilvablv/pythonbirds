class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    cris = Pessoa(nome='Cris')
    ricardo = Pessoa(cris, nome='Ricardo')
    print(Pessoa.cumprimentar(ricardo))
    print(ricardo.nome)
    print(ricardo.idade)
    for filho in ricardo.filhos:
        print((filho.nome))

