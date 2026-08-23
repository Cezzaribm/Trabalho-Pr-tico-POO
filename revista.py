from item import Item


class Revista(Item):
    def __init__(self, codigo, titulo, edicao, mes):
        super().__init__(codigo, titulo)
        self.edicao = edicao
        self.mes = mes

    def exibir_detalhes(self):
        return (
            f"[REVISTA] Código: {self.codigo} | "
            f"Título: {self.titulo} | "
            f"Edição: {self.edicao} | "
            f"Mês: {self.mes}"
        )