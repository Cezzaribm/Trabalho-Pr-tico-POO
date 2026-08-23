from item import Item


class Livro(Item):
    def __init__(self, codigo, titulo, autor, ano):
        super().__init__(codigo, titulo)
        self.autor = autor
        self.ano = ano

    def exibir_detalhes(self):
        return (
            f"[LIVRO] Código: {self.codigo} | "
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Ano: {self.ano}"
        )