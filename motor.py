"""Funções que fazem o game funcionar."""
import random


class Entrada:
    """Classe com funções para funcionamento do game."""

    def __init__(self):
        """Função inicializadora."""
        super(Entrada, self).__init__()
        self.npc = 0

    def dados_npc(self):
        """Gera numero a ser adivinhado randonicamente."""
        self.npc = random.randint(1000, 9999)
        print(self.npc)
        return self.npc

    def compara_numero(self, num_p):
        """Compara numero digitado pelo player e retorna se acertou."""
        self.numero = int(num_p)
        if self.npc == self.numero:
            return 'Você Acertou'

        lista_npc = list(str(self.npc))
        lista_player = list(str(self.numero))

        lista_resultado = []

        # condigo antigo número na posição correta
        '''for a, num_npc in enumerate(lista_npc):
            for b, num_player in enumerate(lista_player):
                if num_npc == num_player and a == b:
                    lista_resultado.append('correto')
                    lista_npc[a] = ''
                    lista_player[b] = '''

        # codigo otimizado número na posição correta
        for i in range(0, 4):
            if lista_npc[i] == lista_player[i]:
                lista_resultado.append('correto')
                lista_npc[i] = ''  # recebe vazio pq já foi achado na lista
                lista_player[i] = ''  # atribuido vazio pode ter 2 números igu

        # codigo antigo número fora de posição
        '''for aa, num_npc in enumerate(lista_npc):
            print('npc', aa, lista_npc)
            for b, num_player in enumerate(lista_player):
                print('player', b, lista_player)

                if lista_npc[aa] == '':
                    break
                if num_npc == num_player and aa != b:
                    lista_resultado.append('local_errado')
                    lista_npc[aa] = ''
                    lista_player[b] = ''
                    break'''

        # codigo otimizado número fora de posição
        for i in range(0, 4):
            if lista_player[i] == '':
                break
            elif lista_player[i] in lista_npc:
                lista_resultado.append('local_errado')
                # recebe vazio pq já foi achado na lista
                lista_npc[lista_npc.index(lista_player[i])] = ''
                # é atribuido vazio pois no jogo pode ter 2 números iguais
                lista_player[i] = ''

        return lista_resultado
