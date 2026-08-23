class Usuario:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Este usuário não possui empréstimos.")
            return

        print(f"\nEmpréstimos de {self.nome}:")

        for emprestimo in self.emprestimos:
            print(emprestimo.exibir_detalhes())