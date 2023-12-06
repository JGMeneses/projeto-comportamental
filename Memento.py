# O originador tem alguns dados importantes que podem mudar com
# o tempo. Ele também define um método para salvar seu estado
# dentro de um memento e outro método para restaurar o estado
# dele.
class Editor:
    def __init__(self):
        self.texto = ""
        self.posicaoX = 0
        self.posicaoY = 0
        self.larguraSelecao = 0

    def definir_texto(self, texto):
        self.texto = texto

    def definir_cursor(self, x, y):
        self.posicaoX = x
        self.posicaoY = y

    def definir_largura_selecao(self, largura):
        self.larguraSelecao = largura

    # Salva o estado atual dentro de um memento.
    def criar_snapshot(self):
        # O memento é um objeto imutável; é por isso que o
        # originador passa seu estado para os parâmetros do
        # construtor do memento.
        return Snapshot(self, self.texto, self.posicaoX, self.posicaoY, self.larguraSelecao)

# A classe memento armazena o estado anterior do editor.
class Snapshot:
    def __init__(self, editor, texto, posicaoX, posicaoY, larguraSelecao):
        self.editor = editor
        self.texto = texto
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY
        self.larguraSelecao = larguraSelecao

    # Em algum momento, um estado anterior do editor pode ser
    # restaurado usando um objeto memento.
    def restaurar(self):
        self.editor.definir_texto(self.texto)
        self.editor.definir_cursor(self.posicaoX, self.posicaoY)
        self.editor.definir_largura_selecao(self.larguraSelecao)

# Um objeto comando pode agir como cuidador. Neste caso, o
# comando obtém o memento antes que ele mude o estado do
# originador. Quando o undo(desfazer) é solicitado, ele
# restaura o estado do originador a partir de um memento.
class Comando:
    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def fazer_backup(self):
        self.backup = self.editor.criar_snapshot()

    def desfazer(self):
        if self.backup is not None:
            self.backup.restaurar()
# ...
