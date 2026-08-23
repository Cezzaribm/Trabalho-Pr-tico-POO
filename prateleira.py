class Prateleira:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.exemplares = []

    def adicionar_exemplar(self, exemplar):
        if exemplar not in self.exemplares:
            self.exemplares.append(exemplar)
            exemplar.colocar_na_prateleira(self)

    def remover_exemplar(self, exemplar):
        if exemplar in self.exemplares:
            self.exemplares.remove(exemplar)
            exemplar.remover_da_prateleira()

    def listar_exemplares(self):
        if not self.exemplares:
            print("Nenhum exemplar nesta prateleira.")
            return

        print(f"\nPrateleira: {self.nome}")

        for exemplar in self.exemplares:
            print(exemplar.exibir_detalhes())