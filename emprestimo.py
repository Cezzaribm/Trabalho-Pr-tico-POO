from datetime import date


class Emprestimo:
    def __init__(self, codigo, usuario, exemplar):
        self.codigo = codigo
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = date.today()
        self.data_devolucao = None
        self.ativo = True

    def finalizar(self):
        self.data_devolucao = date.today()
        self.ativo = False
        self.exemplar.disponivel = True

    def exibir_detalhes(self):
        status = "Ativo" if self.ativo else "Finalizado"

        return (
            f"Empréstimo {self.codigo} | "
            f"Usuário: {self.usuario.nome} | "
            f"Item: {self.exemplar.item.titulo} | "
            f"Data: {self.data_emprestimo.strftime('%d/%m/%Y')} | "
            f"Status: {status}"
        )