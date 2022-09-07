class Pessoa:
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    larissa = Pessoa(nome='Larissa')
    roberth = Pessoa(larissa, nome='Roberth')
    print(Pessoa.cumprimentar(roberth))
    print(id(roberth))
    print(roberth.cumprimentar())
    print(roberth.nome)
    print(roberth.idade)
    for filho in roberth.filhos:
        print(filho.nome)
