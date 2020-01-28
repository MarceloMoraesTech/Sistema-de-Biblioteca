import ListSplit

def registerBook():
    bookname=input("Digite o titulo do livro que deseja doar:")
    authorname=input("Digite o nome do autor do livro que deseja doar:")
    quantity=int(input("Digite a quantidade de livros:"))
    ano=int(input("Digite o ano que o livro foi publicado:"))
    info=bookname+authorname+str(quantity)+str(ano)

    arquivo=open("Stock.txt","r")
    conteudo=arquivo.readlines()

    conteudo.append(info)

    arquivo=open("stock.txt", "w")
    arquivo.writelines(conteudo)
    arquivo.close()

    valores=0
    ref_arquivo = open("Stock.txt","r")
    for linha in ref_arquivo:
        valores = linha.split()

    ref_arquivo.close()


registerBook()
