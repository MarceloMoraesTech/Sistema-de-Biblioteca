import ListSplit
def returnBook():
    name=input("Digite o nome do associado: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip() for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("O nome do associado está incorreto.")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Sistema da Biblioteca Caribe \n")
        f.write("                   Devolvido por: "+ name+"\n")
        f.write("N.\t\tTítulo\t\t Autor\t\t Ano\n")

    
    for i in range(3):
        if ListSplit.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.authorname[i]+"\t\t"+ListSplit.ano[i]+"\n")
                ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
            ListSplit.ano[i]=str(ListSplit.ano[i])
                
        
    with open("Stock.txt","w+") as f:
            for i in range(3):
                f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+ListSplit.ano[i]+"\n")
