#Vinicius Nascimento

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
        else:
            print('Livro ja emprestado')    

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
        else:
            print('Livro ja devolvido')    

class Biblioteca:
    def __init__(self):
        self.lista = []

    def adicionar_livro(self,livro):
        self.lista.append(livro)
        
    def listar_livro(self):
        for livro in self.lista:
            print(f'\n Titulo: {livro.titulo}\n Autor: {livro.autor}\n ISBN: {livro.isbn}')
            if livro.disponivel == True:
                print(" Livro Disponivel")
            else:
                print(" Livro indisponivel")   

    def emprestar_livro(self, codigo):
        for livro in self.lista:
            if livro.isbn == codigo:
                if livro.emprestar():
                    print("Você emprestou esse livro da biblioteca")
                else:
                    print("Livro já emprestado")
                return
        print("Código inválido")
                    
    def devolver_livro(self, codigo):
        for livro in self.lista:
            if livro.isbn == codigo:
                if livro.devolver():
                    print("Você devolveu esse livro da biblioteca")
                else:
                    print("Livro já devolvido")
                return
        print("Código inválido")
                
livro1 = Livro("Diário de um Banana 1", "Alexandre Boide", 8576831309)    
livro2 = Livro("O Menino Maluquinho", "Ilustrador", 6555395656)
livro3 = Livro("Messi: o Gênio Completo", "Ariel Senosiain", 6599666752)
livro4 = Livro("Cristiano Ronaldo: The Biography", "Guillem Balague", 1474611567)


livro = Biblioteca()
livro.adicionar_livro(livro1)
livro.adicionar_livro(livro2)
livro.adicionar_livro(livro3)
livro.adicionar_livro(livro4)

livro.emprestar_livro(8576831309)
livro.emprestar_livro(6555395656)
livro.emprestar_livro(6599666752)
livro.emprestar_livro(1474611567)

livro.devolver_livro(8576831309)
livro.listar_livro()

