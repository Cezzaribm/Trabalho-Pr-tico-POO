class Item:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo

    def exibir_detalhes(self):
        return f"Código: {self.codigo} | Título: {self.titulo}"