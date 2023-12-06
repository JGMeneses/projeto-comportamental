class GameAI:
    # O método padrão define o esqueleto de um algoritmo.
    def turno(self):
        self.coletarRecursos()
        self.construirEstruturas()
        self.construirUnidades()
        self.atacar()

    # Algumas das etapas serão implementadas diretamente na
    # classe base.
    def coletarRecursos(self):
        for s in self.estruturasConstruidas:
            s.coletar()

    # E algumas delas podem ser definidas como abstratas.
    def construirEstruturas(self):
        pass

    def construirUnidades(self):
        pass

    # Uma classe pode ter vários métodos padrão.
    def atacar(self):
        inimigo = self.inimigoMaisProximo()
        if inimigo is None:
            self.enviarExploradores(self.mapa.centro)
        else:
            self.enviarGuerreiros(inimigo.posicao)

    def enviarExploradores(self, posicao):
        pass

    def enviarGuerreiros(self, posicao):
        pass


# Classes concretas têm que implementar todas as operações
# abstratas da classe base, mas não podem sobrescrever o método
# padrão em si.
class OrcsAI(GameAI):
    def construirEstruturas(self):
        if self.haRecursos:
            # Construir fazendas, depois quartéis, e então uma
            # fortaleza.
            pass

    def construirUnidades(self):
        if self.recursosAbundantes:
            if not self.semExploradores:
                # Construir peão, adicionar ele ao grupo de
                # exploradores.
                pass
            else:
                # Construir um bruto, adicionar ele ao grupo
                # dos guerreiros.
                pass

    # ...

    def enviarExploradores(self, posicao):
        if len(self.exploradores) > 0:
            # Enviar exploradores para a posição.
            pass

    def enviarGuerreiros(self, posicao):
        if len(self.guerreiros) > 5:
            # Enviar guerreiros para a posição.
            pass


# As subclasses também podem sobrescrever algumas operações com
# uma implementação padrão.
class MonstersAI(GameAI):
    def coletarRecursos(self):
        # Monstros não coletam recursos.
        pass

    def construirEstruturas(self):
        # Monstros não constroem estruturas.
        pass

    def construirUnidades(self):
        # Monstros não constroem unidades.
        pass
