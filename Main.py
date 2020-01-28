import Return
import ListSplit
import Borrow

def start():
    while(True):
        print("        Bem vindo ao sistema da biblioteca Caribe     ")
        print("------------------------------------------------------")
        print("Digite 1. Para mostrar os livros")
        print("Digite 2. Para retirar um livro")
        print("Digite 3. Para devolver um livro")
        print("Digite 4. Para sair")
        try:
            a=int(input("Escolha uma opção de 1-4: "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Obrigado por usar o site da Biblioteca Caribe Online")
                break
            else:
                print("Por favor digite uma escolha valida de 1-4")
        except ValueError:
            print("Por favor digite como sugerido.")
start()
