# Representa um commit: guarda quem fez, o que fez e qual commit veio antes dele
class Commit:
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Imprime este commit e depois pede pro pai imprimir o dele, até o primeiro commit
    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        if self.pai is None:
            return
        self.pai.historico()