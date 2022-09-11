class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42
    
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    larissa = Mutante(nome = 'Larissa')
    roberth = Homem(larissa, nome = 'Roberth')
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
    print(Pessoa.metodo_estatico(), roberth.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), roberth.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(roberth, Pessoa))
    print(isinstance(roberth, Homem))
    print(larissa.olhos)
    print(roberth.cumprimentar())
    print(larissa.cumprimentar())