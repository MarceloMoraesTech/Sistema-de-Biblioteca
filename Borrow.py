import ListSplit

def borrowBook():
    success=False
    while(True):
        firstName=input("Digite o primeiro nome do associado: ")
        if firstName.isalpha():
            break
        print("Por favor, use letras do alfabeto de A-Z")
    while(True):
        lastName=input("Digite o sobrenome do associado: ")
        if lastName.isalpha():
            break
        print("Por favor, use letras do alfabeto de A-Z")
            
    t="Borrow-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("               Sistema da Biblioteca Caribe  \n")
        f.write("                   Retirado por: "+ firstName+" "+lastName+"\n")
        f.write("N. \t\t Título \t      Autor \t Ano \n" )
    
    while success==False:
        print("Por favor, selecione uma opção abaixo:")
        for i in range(len(ListSplit.bookname)):
            print("Digite", i, "para retirar livro", ListSplit.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.quantity[a])>0):
                    print("Este livro está disponível.")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\t\t"+ListSplit.ano[i]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+ListSplit.ano[i]+"\n")


                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Você deseja retirar mais algum livro? Lembre que você não pode pegar o mesmo livro duas vezes. Digite S pra sim e N pra não."))
                        if(choice.upper()=="S"):
                            count=count+1
                            print("Por favor selecione uma opção abaixo:")
                            for i in range(len(ListSplit.bookname)):
                                print("Digite", i, "para retirar livro", ListSplit.bookname[i])
                            a=int(input())
                            if(int(ListSplit.quantity[a])>0):
                                print("O livro está disponível.")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                                ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+ListSplit.ano[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Obrigado por retirar livros conosco. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Por favor, faça como foi instruido")
                        
                else:
                    print("Este livro não está disponível")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Por favor, escolha o livro de acordo com o número dele.")
        except ValueError:
            print("")
            print("Por favor, faça de acordo com o sugerido.")
