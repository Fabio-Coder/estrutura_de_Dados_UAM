class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, dado):
        return self.dados.append(dado)

    def desempilha(self):
        return self.dados.pop(-1)

    def imprime_pilha(self):
        for i in range(len(self.dados)):
            print(self.dados[i], end=' ')
        print('')

    def quantos_elementos(self):
        return len(self.dados)

    def e_vazia(self):
        if len(self.dados) == 0:
            return True
        else:
            return False
