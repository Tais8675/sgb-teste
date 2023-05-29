class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def remover_livro(self, livro):
        self.livros.remove(livro)
        print(f"Livro '{livro.titulo}' removido da biblioteca.")

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def buscar_livro_por_autor(self, autor):
        for livro in self.livros:
            if livro.autor.lower() == autor.lower():
                return livro
        return None

    def buscar_livro_por_categoria(self, categoria):
        livros_encontrados = []
        for livro in self.livros:
            if livro.categoria.lower() == categoria.lower():
                livros_encontrados.append(livro)
        return livros_encontrados
    
  


    def listar_livros(self):
        if len(self.livros) > 0:
            print("Livros na biblioteca:")
            for livro in self.livros:
                print(f"{livro.titulo} - {livro.autor}")
        else:
            print("A biblioteca não possui livros.")

    def listar_livros_emprestados(self):
        livros_emprestados = [livro for livro in self.livros if livro.emprestado]
        if len(livros_emprestados) > 0:
            print("Livros emprestados:")
            for livro in livros_emprestados:
                print(f"{livro.titulo} - {livro.autor}")
        else:
            print("A biblioteca não possui livros emprestados.")


class Livro:
    def __init__(self, titulo, autor, editora, categoria, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria
        self.num_copias = num_copias
        self.emprestado = False

    def emprestar(self):
        if self.num_copias > 0:
            self.num_copias -= 1
            self.emprestado = True
            print(f"Livro '{self.titulo}' emprestado.")
        else:
            print("Não há cópias disponíveis deste livro.")

    def devolver(self):
        self.num_copias += 1
        self.emprestado = False
        print(f"Livro '{self.titulo}' devolvido à biblioteca.")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

    def pegar_livro_emprestado(self, biblioteca, titulo):
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            if livro.emprestado:
                print(f"Livro '{livro.titulo}' não está disponível no momento.")
            else:
                livro.emprestar()
                self.emprestimos.append(livro)
                print(f"{self.nome} pegou emprestado o livro '{livro.titulo}'.")
        else:
            print("Livro não encontrado.")

    def devolver_livro(self, biblioteca, titulo):
        for livro in self.emprestimos:
            if livro.titulo == titulo:
                livro.devolver()
                self.emprestimos.remove(livro)
                print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
                return
        print("Livro não encontrado nos empréstimos do usuário.")

    def listar_emprestimos(self):
        if len(self.emprestimos) > 0:
            print(f"Empréstimos do usuário {self.nome}:")
            for livro in self.emprestimos:
                print(f"{livro.titulo} - {livro.autor}")
        else:
            print("O usuário não possui livros emprestados.")

  


biblioteca = Biblioteca()

while True:
    print("Selecione uma opção:")
    print("1 - Adicionar um livro à biblioteca")
    print("2 - Remover um livro da biblioteca")
    print("3 - Buscar um livro na biblioteca pelo título, autor ou categoria")
    print("4 - Listar todos os livros da biblioteca")
    print("5 - Registrar um empréstimo de um livro")
    print("6 - Registrar a devolução de um livro")
    print("7 - Listar todos os livros emprestados")
    print("0 - Sair do programa")

    opcao = input()

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        editora = input("Digite a editora do livro: ")
        categoria = input("Digite a categoria do livro: ")
        num_copias = int(input("Digite o número de cópias disponíveis do livro: "))
        livro = Livro(titulo, autor, editora, categoria, num_copias)
        biblioteca.adicionar_livro(livro)

    elif opcao == "2":
        titulo = input("Digite o título do livro que deseja remover: ")
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            biblioteca.remover_livro(livro)
        else:
            print("Livro não encontrado.")

    elif opcao == "3":
        print("Escolha a opção de busca:")
        print("1 - Buscar livro por título")
        print("2 - Buscar livro por autor")
        print("3 - Buscar livro por categoria")

        opcao_busca = input()

        if opcao_busca == "1":
            termo = input("Digite o título do livro que deseja buscar: ")
            livro = biblioteca.buscar_livro_por_titulo(termo)


        elif opcao_busca == "2":
            termo = input("Digite o autor do livro que deseja buscar: ")
            livro = biblioteca.buscar_livro_por_autor(termo)


        elif opcao_busca == "3":
            termo = input("Digite a categoria do livro que deseja buscar: ")
            livros_encontrados = biblioteca.buscar_livro_por_categoria(termo)
            if len(livros_encontrados) > 0:
                print(f"Livros encontrados na categoria '{termo}':")
                for livro in livros_encontrados:
                    print(f"{livro.titulo} - {livro.autor} - {livro.editora}")
            else:
                print("Nenhum livro encontrado nesta categoria.")
        else:
            print("Opção inválida.")



    elif opcao == "4":
        biblioteca.listar_livros()

    elif opcao == "5":
        titulo = input("Digite o título do livro que deseja emprestar: ")
        usuario_nome = input("Digite o nome do usuário que está pegando emprestado: ")
        usuario = Usuario(usuario_nome)
        usuario.pegar_livro_emprestado(biblioteca, titulo)



    elif opcao == "6":
        titulo = input("Digite o título do livro que deseja devolver: ")
        usuario_nome = input("Digite o nome do usuário que está devolvendo o livro: ")
        usuario = Usuario(usuario_nome)
        usuario.devolver_livro(biblioteca, titulo)



    elif opcao == "7":
        biblioteca.listar_livros_emprestados()

    elif opcao == "0":
        print("Obrigado por utilizar a biblioteca. Até mais!")
        break

    else:
        print("Opção inválida.")
