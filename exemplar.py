class Exemplar:
    def __init__(self, codigo, item):
        self.codigo = codigo
        self.item = item
        self.prateleira = None
        self.disponivel = True

    def colocar_na_prateleira(self, prateleira):
        self.prateleira = prateleira

    def remover_da_prateleira(self):
        self.prateleira = None

    def exibir_detalhes(self):
        if self.prateleira:
            local = self.prateleira.nome
        else:
            local = "Sem prateleira"

        status = "Disponível" if self.disponivel else "Emprestado"

        return (
            f"Exemplar: {self.codigo} | "
            f"{self.item.titulo} | "
            f"Local: {local} | "
            f"Status: {status}"
        )