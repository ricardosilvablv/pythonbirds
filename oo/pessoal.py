class Pessoa:
    def __init__(self):
        self.nome = None

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(p.nome)