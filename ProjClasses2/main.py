cont = 100
obj = []
ins = []
obj2 = []
ins2 = []
objprod = []
objprod2 = []
insprod = []
insprod2 = []
prodatb = []

while(cont != 0):
    print("1 - Cliente")
    print("2 - Produto")
    print("3 - Fazer uma busca")
    print("0 - Sair")
    print("Escolhida: ")
    x = int(input())
    if(x == 1):
        print("--Informe o Metodo de Inserção Cliente--")
        print("1 - Manual")
        print("2 - Listar Manual e inserir no MongoDB")
        print("3 - Planilha")
        print("4 - Listar Planilha e inserir no MongoDB")
        print("0 - Voltar")
        print("Escolhida: ")
        y = int(input())
        if(y == 1):
            print("---Informe os Dados---")
            print("ID: ")
            a = input()
            print("Nome: ")
            b = input()
            print("Telefone: ")
            c = input()
            print("Endereço: ")
            d = input()
            print("Cidade: ")
            e = input()
            print("Estado: ")
            f = input()
            print("Nascimento:")
            g = input()
            print("-----------------------------")
            z = Cliente(a, b, c, d, e, f, g)
            obj.append(z)

        elif(y == 2):
            i = 0
            while i < len(obj):
                print("-----------------------------")
                print((" ID : {} \n Nome : {} \n Telefone : {} \n Endereço : {} \n Cidade : {} \n Estado : {} \n Nascimento : {} \n").format(obj[i].getID(),
                    obj[i].getNome(), obj[i].getTelefone(), obj[i].getEndereco(), obj[i].getCidade(), obj[i].getEstado(), obj[i].getNasc()))
                print("-----------------------------")
                ins.append({"ID" : obj[i].getID(),
                            "Nome" : obj[i].getNome(),
                            "Telefone" : obj[i].getTelefone(),
                            "Endereco" : obj[i].getEndereco(),
                            "Cidade" : obj[i].getCidade(),
                            "Estado" : obj[i].getEstado(),
                            "Nascimento" : obj[i].getNasc()})
                i += 1
            clientcol1.insert_many(ins)