class Venda:
    def __init__(self, ID, descricao, produto, funcionario, cliente, data):
        self.ID = ID
        self.descricao = descricao
        self.produto = produto
        self.funcionario = funcionario
        self.cliente = cliente
        self.data = data

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao (self):
        return self.descricao

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getFunc (self):
        return self.funcionario

    def getProd (self):
        return self.produto

    def getCliente (self):
        return self.cliente