class Produto:
    def __init__(self, ID, descricao, preco, entrada, saida):
        self.ID = ID
        self.descricao = descricao
        self.preco = preco
        self.entrada = entrada
        self.saida = saida

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao (self):
        return self.descricao

    def setPreco(self, preco):
        self.preco = preco

    def getPreco (self):
        return self.preco

    def setEntrada(self, entrada):
        self.entrada = entrada

    def getEntrada (self):
        return self.entrada

    def setSaida(self, saida):
        self.saida = saida

    def getSaida (self):
        return self.saida