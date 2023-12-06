# A classe publicadora base inclui o código de gerenciamento de
# inscrições e os métodos de notificação.
class GerenciadorEventos:
    def __init__(self):
        self.ouvintes = {}

    def inscrever(self, tipoEvento, ouvinte):
        if tipoEvento in self.ouvintes:
            self.ouvintes[tipoEvento].append(ouvinte)
        else:
            self.ouvintes[tipoEvento] = [ouvinte]

    def cancelar_inscricao(self, tipoEvento, ouvinte):
        if tipoEvento in self.ouvintes and ouvinte in self.ouvintes[tipoEvento]:
            self.ouvintes[tipoEvento].remove(ouvinte)

    def notificar(self, tipoEvento, dados):
        if tipoEvento in self.ouvintes:
            for ouvinte in self.ouvintes[tipoEvento]:
                ouvinte.atualizar(dados)


# O publicador concreto contém a verdadeira lógica de negócio
# que é de interesse para alguns assinantes. Nós podemos
# derivar essa classe a partir do publicador base, mas isso nem
# sempre é possível na vida real devido a possibilidade do
# publicador concreto já ser uma subclasse. Neste caso, você
# pode remendar a lógica de inscrição com a composição, como
# fizemos aqui.
class Editor:
    def __init__(self):
        self.eventos = GerenciadorEventos()
        self.arquivo = None

    # Métodos da lógica de negócio podem notificar assinantes
    # acerca de mudanças.
    def abrir_arquivo(self, caminho):
        self.arquivo = Arquivo(caminho)
        self.eventos.notificar("abrir", self.arquivo.nome)

    def salvar_arquivo(self):
        self.arquivo.escrever()
        self.eventos.notificar("salvar", self.arquivo.nome)

    # ...


# Aqui é a interface do assinante. Se sua linguagem de
# programação suporta tipos funcionais, você pode substituir
# toda a hierarquia do assinante por um conjunto de funções.
class OuvinteEvento:
    def atualizar(self, nome_arquivo):
        pass


# Assinantes concretos reagem a atualizações emitidas pelo
# publicador a qual elas estão conectadas.
class OuvinteLog(OuvinteEvento):
    def __init__(self, nome_arquivo_log, mensagem):
        self.log = Arquivo(nome_arquivo_log)
        self.mensagem = mensagem

    def atualizar(self, nome_arquivo):
        self.log.escrever(self.mensagem.replace('%s', nome_arquivo))


class OuvinteAlertaEmail(OuvinteEvento):
    def __init__(self, email, mensagem):
        self.email = email
        self.mensagem = mensagem

    def atualizar(self, nome_arquivo):
        sistema.enviar_email(self.email, self.mensagem.replace('%s', nome_arquivo))


# Uma aplicação pode configurar publicadores e assinantes
# durante o tempo de execução.
class Aplicacao:
    def configurar(self):
        editor = Editor()

        logger = OuvinteLog(
            "/caminho/para/log.txt",
            "Alguém abriu o arquivo: %s")
        editor.eventos.inscrever("abrir", logger)

        alertas_email = OuvinteAlertaEmail(
            "admin@exemplo.com",
            "Alguém modificou o arquivo: %s")
        editor.eventos.inscrever("salvar", alertas_email)
