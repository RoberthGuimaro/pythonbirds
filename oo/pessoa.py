class Pessoa:
    olhos = 2
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
    roberth.sobrenome = 'Guimaro'
    del roberth.filhos
    roberth.olhos = 1
    del roberth.olhos
    print(roberth.__dict__)
    print(larissa.__dict__)
    print(Pessoa.olhos)
    print(roberth.olhos)
    print(larissa.olhos)
    print(id(Pessoa.olhos), id(roberth.olhos), id(larissa.olhos))