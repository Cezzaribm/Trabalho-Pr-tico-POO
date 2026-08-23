from prateleira import Prateleira
from emprestimo import Emprestimo


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []
        self.exemplares = []
        self.usuarios = []
        self.emprestimos = []

        # Composição: a Biblioteca cria suas próprias prateleiras
        self.prateleiras = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def adicionar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def criar_prateleira(self, codigo, nome):
        prateleira = Prateleira(codigo, nome)
        self.prateleiras.append(prateleira)
        return prateleira

    def remover_prateleira(self, codigo):
        for prateleira in self.prateleiras:
            if prateleira.codigo == codigo:

                # Os exemplares continuam existindo.
                for exemplar in prateleira.exemplares:
                    exemplar.remover_da_prateleira()

                self.prateleiras.remove(prateleira)

                print("Prateleira removida.")
                print("Os exemplares continuam cadastrados na biblioteca.")
                return

        print("Prateleira não encontrada.")

    def realizar_emprestimo(self, codigo_emprestimo, usuario, exemplar):
        if not exemplar.disponivel:
            print("Este exemplar já está emprestado.")
            return None

        emprestimo = Emprestimo(
            codigo_emprestimo,
            usuario,
            exemplar
        )

        exemplar.disponivel = False

        self.emprestimos.append(emprestimo)
        usuario.adicionar_emprestimo(emprestimo)

        print("Empréstimo realizado com sucesso.")

        return emprestimo

    def realizar_devolucao(self, codigo_emprestimo):
        for emprestimo in self.emprestimos:
            if emprestimo.codigo == codigo_emprestimo:

                if not emprestimo.ativo:
                    print("Este empréstimo já foi finalizado.")
                    return

                emprestimo.finalizar()

                print("Devolução realizada com sucesso.")
                return

        print("Empréstimo não encontrado.")

    def listar_itens(self):
        if not self.itens:
            print("Nenhum item cadastrado.")
            return

        print("\n===== ITENS DA BIBLIOTECA =====")

        for item in self.itens:
            # POLIMORFISMO
            print(item.exibir_detalhes())

    def listar_exemplares(self):
        if not self.exemplares:
            print("Nenhum exemplar cadastrado.")
            return

        print("\n===== EXEMPLARES =====")

        for exemplar in self.exemplares:
            print(exemplar.exibir_detalhes())

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return

        print("\n===== USUÁRIOS =====")

        for usuario in self.usuarios:
            print(
                f"Código: {usuario.codigo} | "
                f"Nome: {usuario.nome}"
            )