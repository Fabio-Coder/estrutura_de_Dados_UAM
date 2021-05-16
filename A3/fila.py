class Fila(object):
    def __init__(self):
        self.dados = []

    def insere(self, dado):
        self.dados.append(dado)

    def retira(self):
        self.dados.pop(0)

    def insere_na_posicao(self, posicao, dado):
        self.dados[posicao] = dado

    def insere_no_inicio(self, dado):
        self.dados.insert(0,dado)
        self.dados.pop(-1)

    def imprime_fila(self):
        for i in range(len(self.dados)):
            print(self.dados[i], end=' ')
        print(' ')

    def quantos_elementos(self):
        return len(self.dados)

    def e_vazia(self):
        if len(dados) == 0:
            return True
        else:
            return False
