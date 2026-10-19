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


# Representa o repositório: guarda o commit mais recente (head) e conta os commits
class Repositorio:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador = 0

    # Cria um commit novo com id único, ligado ao head atual, e vira o novo head
    def commitar(self, mensagem):
        self.contador = self.contador + 1
        novo_commit = Commit(self.contador, mensagem, self.autor, self.head)
        self.head = novo_commit

    # Mostra o histórico do mais novo pro mais antigo
    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return
        self.head.historico()

    # Anda de pai em pai a partir do head contando quantos commits existem
    def total_de_commits(self):
        total = 0
        atual = self.head
        while atual is not None:
            total = total + 1
            atual = atual.pai
        return total