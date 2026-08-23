from biblioteca import Biblioteca
from livro import Livro
from revista import Revista
from exemplar import Exemplar
from usuario import Usuario


biblioteca = Biblioteca("Biblioteca IFMG")


def cadastrar_livro():
    codigo = input("Código do livro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")

    livro = Livro(codigo, titulo, autor, ano)

    biblioteca.adicionar_item(livro)

    print("Livro cadastrado com sucesso.")


def cadastrar_revista():
    codigo = input("Código da revista: ")
    titulo = input("Título: ")
    edicao = input("Edição: ")
    mes = input("Mês: ")

    revista = Revista(codigo, titulo, edicao, mes)

    biblioteca.adicionar_item(revista)

    print("Revista cadastrada com sucesso.")


def cadastrar_exemplar():
    if not biblioteca.itens:
        print("Cadastre um livro ou revista primeiro.")
        return

    biblioteca.listar_itens()

    codigo_item = input("\nDigite o código do item: ")

    item_encontrado = None

    for item in biblioteca.itens:
        if item.codigo == codigo_item:
            item_encontrado = item
            break

    if item_encontrado is None:
        print("Item não encontrado.")
        return

    codigo_exemplar = input("Código do exemplar: ")

    exemplar = Exemplar(codigo_exemplar, item_encontrado)

    biblioteca.adicionar_exemplar(exemplar)

    print("Exemplar cadastrado com sucesso.")


def cadastrar_usuario():
    codigo = input("Código do usuário: ")
    nome = input("Nome: ")

    usuario = Usuario(codigo, nome)

    biblioteca.adicionar_usuario(usuario)

    print("Usuário cadastrado com sucesso.")


def criar_prateleira():
    codigo = input("Código da prateleira: ")
    nome = input("Nome da prateleira: ")

    biblioteca.criar_prateleira(codigo, nome)

    print("Prateleira criada com sucesso.")


def colocar_exemplar_na_prateleira():
    if not biblioteca.exemplares:
        print("Nenhum exemplar cadastrado.")
        return

    if not biblioteca.prateleiras:
        print("Nenhuma prateleira cadastrada.")
        return

    biblioteca.listar_exemplares()

    codigo_exemplar = input("\nCódigo do exemplar: ")

    exemplar_encontrado = None

    for exemplar in biblioteca.exemplares:
        if exemplar.codigo == codigo_exemplar:
            exemplar_encontrado = exemplar
            break

    if exemplar_encontrado is None:
        print("Exemplar não encontrado.")
        return

    print("\n===== PRATELEIRAS =====")

    for prateleira in biblioteca.prateleiras:
        print(
            f"Código: {prateleira.codigo} | "
            f"Nome: {prateleira.nome}"
        )

    codigo_prateleira = input("Código da prateleira: ")

    for prateleira in biblioteca.prateleiras:
        if prateleira.codigo == codigo_prateleira:
            prateleira.adicionar_exemplar(exemplar_encontrado)
            print("Exemplar colocado na prateleira.")
            return

    print("Prateleira não encontrada.")


def realizar_emprestimo():
    if not biblioteca.usuarios:
        print("Cadastre um usuário primeiro.")
        return

    if not biblioteca.exemplares:
        print("Cadastre um exemplar primeiro.")
        return

    biblioteca.listar_usuarios()

    codigo_usuario = input("\nCódigo do usuário: ")

    usuario = None

    for u in biblioteca.usuarios:
        if u.codigo == codigo_usuario:
            usuario = u
            break

    if usuario is None:
        print("Usuário não encontrado.")
        return

    biblioteca.listar_exemplares()

    codigo_exemplar = input("\nCódigo do exemplar: ")

    exemplar = None

    for e in biblioteca.exemplares:
        if e.codigo == codigo_exemplar:
            exemplar = e
            break

    if exemplar is None:
        print("Exemplar não encontrado.")
        return

    codigo_emprestimo = input("Código do empréstimo: ")

    biblioteca.realizar_emprestimo(
        codigo_emprestimo,
        usuario,
        exemplar
    )


def realizar_devolucao():
    if not biblioteca.emprestimos:
        print("Nenhum empréstimo cadastrado.")
        return

    print("\n===== EMPRÉSTIMOS =====")

    for emprestimo in biblioteca.emprestimos:
        print(emprestimo.exibir_detalhes())

    codigo = input("\nCódigo do empréstimo: ")

    biblioteca.realizar_devolucao(codigo)


def listar_prateleiras():
    if not biblioteca.prateleiras:
        print("Nenhuma prateleira cadastrada.")
        return

    for prateleira in biblioteca.prateleiras:
        prateleira.listar_exemplares()


def listar_emprestimos():
    if not biblioteca.emprestimos:
        print("Nenhum empréstimo cadastrado.")
        return

    print("\n===== EMPRÉSTIMOS =====")

    for emprestimo in biblioteca.emprestimos:
        print(emprestimo.exibir_detalhes())


def menu():
    while True:
        print("\n")
        print("====================================")
        print("       SISTEMA DE BIBLIOTECA")
        print("====================================")
        print("1 - Cadastrar livro")
        print("2 - Cadastrar revista")
        print("3 - Cadastrar exemplar")
        print("4 - Cadastrar usuário")
        print("5 - Criar prateleira")
        print("6 - Colocar exemplar na prateleira")
        print("7 - Listar itens")
        print("8 - Listar exemplares")
        print("9 - Listar prateleiras")
        print("10 - Realizar empréstimo")
        print("11 - Realizar devolução")
        print("12 - Listar empréstimos")
        print("13 - Listar usuários")
        print("14 - Remover prateleira")
        print("0 - Sair")
        print("====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()

        elif opcao == "2":
            cadastrar_revista()

        elif opcao == "3":
            cadastrar_exemplar()

        elif opcao == "4":
            cadastrar_usuario()

        elif opcao == "5":
            criar_prateleira()

        elif opcao == "6":
            colocar_exemplar_na_prateleira()

        elif opcao == "7":
            biblioteca.listar_itens()

        elif opcao == "8":
            biblioteca.listar_exemplares()

        elif opcao == "9":
            listar_prateleiras()

        elif opcao == "10":
            realizar_emprestimo()

        elif opcao == "11":
            realizar_devolucao()

        elif opcao == "12":
            listar_emprestimos()

        elif opcao == "13":
            biblioteca.listar_usuarios()

        elif opcao == "14":
            codigo = input("Código da prateleira a remover: ")
            biblioteca.remover_prateleira(codigo)

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


menu()