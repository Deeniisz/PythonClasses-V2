from Cliente import Cliente
from Produto import Produto
from Funcionario import Funcionario
from Venda import Venda
import xlrd
import pymongo
import urllib.request
from bs4 import BeautifulSoup
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb1 = myclient["cliente"]
clientcol1 = mydb1["manual"]
clientcol2 = mydb1["planilha"]

mydb2 = myclient["produto"]
produtocol1 = mydb2["manual"]
produtocol2 = mydb2["planilha"]
produtocol3 = mydb2["site"]

mydb3 = myclient["func"]
funccol1 = mydb3["manual"]

mydb3 = myclient["venda"]
vendacol1 = mydb3["listavenda"]

cont = 100
obj = []
ins = []
obj2 = []
ins2 = []
obj3 = []
ins3 = []
obj4 = []
ins4 = []
objprod = []
objprod2 = []
insprod = []
insprod2 = []
prodatb = []

while(cont != 0):
    print("1 - Cliente")
    print("2 - Produto")
    print("3 - Fazer uma busca")
    print("4 - Funcionario")
    print("5 - Gerar uma Venda")
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

        if (y == 1):

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


        elif (y == 2):
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

        elif (y == 3):
            book = xlrd.open_workbook("cliente.xls")

            sh = book.sheet_by_index(0)

            print("-----------------------------")
            print("A Planilha Foi Lida !")
            print("-----------------------------")

            i = 1
            while i < 6:
                a = int(sh.cell_value(rowx=0, colx=i))
                b = (sh.cell_value(rowx=1, colx=i))
                c = (sh.cell_value(rowx=2, colx=i))
                d = (sh.cell_value(rowx=3, colx=i))
                e = (sh.cell_value(rowx=4, colx=i))
                f = (sh.cell_value(rowx=5, colx=i))
                g = str(sh.cell_value(rowx=6, colx=i))

                x = Cliente(a, b, c, d, e, f, g)

                obj2.append(x)
                i += 1

        elif (y == 4):
            i = 0
            while i < 5:

                print("-----------------------------")
                print((" ID : {} \n Nome : {} \n Telefone : {} \n Endereço : {} \n Cidade : {} \n Estado : {} \n Nascimento : {} \n").format(
                    obj2[i].getID(), obj2[i].getNome(), obj2[i].getTelefone(), obj2[i].getEndereco(), obj2[i].getCidade(), obj2[i].getEstado(), obj2[i].getNasc()))
                print("-----------------------------")

                ins2.append({"ID": obj2[i].getID(),
                            "Nome": obj2[i].getNome(),
                            "Telefone": obj2[i].getTelefone(),
                            "Endereco": obj2[i].getEndereco(),
                            "Cidade": obj2[i].getCidade(),
                            "Estado": obj2[i].getEstado(),
                            "Nascimento": obj2[i].getNasc()})



                i += 1

            clientcol2.insert_many(ins2)

        elif (y == 0):
            pass

    elif(x == 2):
        print("--Informe o Metodo de Inserção PRODUTO--")
        print("1 - Manual")
        print("2 - Listar Manual e inserir no MongoDB")
        print("3 - Planilha")
        print("4 - Listar Planilha e inserir no MongoDB")
        print("5 - Ler Site Carrefour")
        print("6 - Listar e inserir Site no MongoDB")
        print("0 - Voltar")
        print("Escolhida: ")
        y = int(input())

        if (y == 1):

            print("---Informe os Dados---")

            print("ID: ")
            a = input()

            print("Nome: ")
            b = input()

            print("Preço: ")
            c = input()

            print("Entrada: ")
            d = input()

            print("Saida: ")
            e = input()

            print("-----------------------------")

            z = Produto(a, b, c, d, e)

            objprod.append(z)

        elif (y == 2):
            i = 0
            while i < len(objprod):
                print("-----------------------------")
                print((" ID : {} \n Nome : {} \n Preço : {} \n Entrada : {} \n Saída : {} \n").format(
                    objprod[i].getID(), objprod[i].getNome(), objprod[i].getPreco(), objprod[i].getEntrada(), objprod[i].getSaida()))
                print("-----------------------------")
                insprod.append({"ID": objprod[i].getID(),
                             "Nome": objprod[i].getNome(),
                             "Preço": objprod[i].getPreco(),
                             "Entrada": objprod[i].getEntrada(),
                             "Saida": objprod[i].getSaida()})
                i += 1
            produtocol1.insert_many(insprod)


        elif (y == 3):
            book = xlrd.open_workbook("produtos.xls")

            sh = book.sheet_by_index(0)

            i = 1
            while i < 6:
                a = int(sh.cell_value(rowx=0, colx=i))
                b = (sh.cell_value(rowx=1, colx=i))
                c = (sh.cell_value(rowx=2, colx=i))
                d = (sh.cell_value(rowx=3, colx=i))
                e = (sh.cell_value(rowx=4, colx=i))

                x = Produto(a, b, c, d, e)

                objprod2.append(x)
                i += 1
            print("-----------------------------")
            print("A Planilha Foi Lida !")
            print("-----------------------------")

        elif (y == 4):
            i = 0
            while i < len(objprod2):
                print("-----------------------------")
                print((" ID : {} \n Nome : {} \n Preço : {} \n Entrada : {} \n Saída : {} \n").format(
                    objprod2[i].getID(), objprod2[i].getNome(), objprod2[i].getPreco(), objprod2[i].getEntrada(), objprod2[i].getSaida()))
                print("-----------------------------")
                insprod2.append({"ID" : objprod2[i].getID(),
                             "Nome" : objprod2[i].getNome(),
                             "Preço" : objprod2[i].getPreco(),
                             "Entrada" : objprod2[i].getEntrada(),
                             "Saida" : objprod2[i].getSaida()})
                i += 1
            produtocol2.insert_many(insprod2)

        elif (y == 5):
            print("Qual Pagina deseja Ler 1-5:")
            pagina = input()
            url = "https://www.carrefour.com.br/busca?termo=Notebook&isGrid=true&sort=&page={}&foodzipzone=na".format(
                pagina)
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

            webpage = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(webpage, "html.parser")

            formatedname = soup.findAll("h3", "prd-name")
            formatedprice = soup.findAll("span", "prd-price-new")

            name = []
            price = []
            dblist = []

            for i in formatedname:
                line = str(i).replace('<h3 class="prd-name">', "").replace("</h3>", "").strip()
                name.append(line)

            for i in formatedprice:
                line = str(i).replace('<span class="prd-price-new">', "").replace("<bdi>", "").replace("</bdi>", "").replace("</span>", "").strip()
                price.append(line)

            i = 0
        elif (y == 6):
            for info in name:
                print(("Nome: {}, Preço: {}").format(name[i], price[i]))

                dblist.append({"ID" : random.randint(0, 999), "Nome": name[i], "Preço": price[i], "Entrada" : "XX/XX/XX", "Saida" : "XX/XX/XX"})
                i += 1
            produtocol3.insert_many(dblist)

        elif (y == 0):
            pass

    elif (x == 3):
        print("----Menu de Busca----")
        print("1 - Cliente")
        print("2 - Produto")
        print("0 - Voltar")
        print("Escolhida:")
        y = int(input())

        if(y == 1):
            print("----Menu de Busca - Cliente----")
            print("1 - Manual")
            print("2 - Planilha")
            print("0 - Voltar")
            print("Escolhida:")
            x = int(input())

            if(x == 1):
                print("-----------------------------")
                print("Informe o nome a ser Buscado:")
                y = str(input())
                i = 0

                while i < len(obj):
                    if y in obj[i].getNome():
                        print("--------------------")
                        print(("Nome Encontrado: {}").format(obj[i].getNome()))
                        print("--------------------")
                    i += 1
            elif(x == 2):
                print("-----------------------------")
                print("Informe o nome a ser Buscado:")
                y = str(input())
                i = 0

                while i < len(obj2):
                    if y in obj2[i].getNome():
                        print("--------------------")
                        print(("Nome Encontrado: {}").format(obj2[i].getNome()))
                        print("--------------------")
                    i += 1
            elif(x == 0):
                pass



        elif(y == 2):
            print("----Menu de Busca - Produto----")
            print("1 - Manual")
            print("2 - Planilha")
            print("3 - Site")
            print("0 - Voltar")
            print("Escolhida:")
            x = int(input())

            if(x == 1):
                print("-----------------------------")
                print("Informe o nome a ser Buscado:")
                x = str(input())
                i = 0

                while i < len(objprod):
                    if x in objprod[i].getNome():
                        print("--------------------")
                        print(("Nome Encontrado: {}").format(objprod[i].getNome()))
                        print("--------------------")
                    i += 1

            elif(x == 2):
                print("-----------------------------")
                print("Informe o nome a ser Buscado:")
                y = str(input())
                i = 0

                while i < len(objprod):
                    if y in objprod2[i].getNome():
                        print("--------------------")
                        print(("Nome Encontrado: {}").format(objprod2[i].getNome()))
                        print("--------------------")
                    i += 1

            elif(x == 3):
                print("-----------------------------")
                print("Informe o nome a ser Buscado:")
                y = str(input())

                i = 0
                while i < len(name):
                    if y in name[i]:
                        print("--------------------")
                        print(("Nome Encontrado: {}").format(name[i]))
                        print("--------------------")
                    i += 1

        elif(y == 0):
            pass

    elif (x == 4):
        print("--Informe o Metodo de Inserção Funcionario--")
        print("1 - Cadastro Manual")
        print("2 - Listar Manual e inserir no MongoDB")
        print("0 - Voltar")
        print("Escolhida: ")
        y = int(input())

        if (y == 1):

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

            print("Salario:")
            h = input()

            print("-----------------------------")

            z = Funcionario(a, b, c, d, e, f, g, h)
            obj3.append(z)


        elif (y == 2):
            i = 0
            while i < len(obj3):
                print("-----------------------------")
                print((" ID : {} \n Nome : {} \n Telefone : {} \n Endereço : {} \n Cidade : {} \n Estado : {} \n Nascimento : {} \n Salario : {} \n").format(obj3[i].getID(),
                    obj3[i].getNome(), obj3[i].getTelefone(), obj3[i].getEndereco(), obj3[i].getCidade(), obj3[i].getEstado(), obj3[i].getNasc(), obj3[i].getSal()))
                print("-----------------------------")
                ins3.append({"ID" : obj3[i].getID(),
                            "Nome" : obj3[i].getNome(),
                            "Telefone" : obj3[i].getTelefone(),
                            "Endereco" : obj3[i].getEndereco(),
                            "Cidade" : obj3[i].getCidade(),
                            "Estado" : obj3[i].getEstado(),
                            "Nascimento" : obj3[i].getNasc(),
                            "Salario" : obj3[i].getSal()})
                i += 1

            funccol1.insert_many(ins3)

        elif (y == 0):
            pass
    
    elif (x == 5):
        print("---Informe os Dados---")

        print("ID da Venda: ")
        a = input()

        print("Descricao: ")
        b = input()

        print("ID do Produto: ")
        c = input()

        i = 0
        while i < len(objprod):
            if c == objprod[i].getID():
                c = objprod[i]
            i += 1   

        print("ID do Funcionario: ")
        d = input()

        i = 0
        while i < len(obj3):
            if d == obj3[i].getID():
                d = obj3[i]
            i += 1 

        print("ID do Cliente: ")
        e = input()

        i = 0
        while i < len(obj):
            if e == obj[i].getID():
                e = obj[i]
            i += 1 

        print("DATA: ")
        f = input()

        print("-----------------------------")

        z = Venda(a, b, c, d, e, f)
        obj4.append(z)
        i = 0
        while i < len(obj4):
            print("-----------------------------")
            print((" ID : {} \n Descricao : {} \n Produto : {} \n Funcionario : {} \n Cliente : {} \n Data : {} \n").format(obj4[i].getID(),
                obj4[i].getDescricao(), obj4[i].getProd(), obj4[i].getFunc(), obj4[i].getCliente(), obj4[i].getData()))
            print("-----------------------------")
            ins4.append({"ID" : obj4[i].getID(),
                        "Descricao" : obj4[i].getDescricao(),
                        "Produto" : obj4[i].getProd().getNome(),
                        "Funcionario" : obj4[i].getFunc().getNome(),
                        "Cliente" : obj4[i].getCliente().getNome(),
                        "Data" : obj4[i].getData()})
            i += 1
    
        vendacol1.insert_many(ins4)

    elif(x == 0):
        break