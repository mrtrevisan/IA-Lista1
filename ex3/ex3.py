class Estado:
    # Construtor da classe Estado 
    # Os atributos representam as posições do fazendeiro, do lobo,
    # da ovelha e do repolho 
    # também é guardado o estado "pai"
    def __init__(self, fazendeiro, lobo, ovelha, repolho, estado_pai):
        self.fazendeiro = fazendeiro
        self.lobo = lobo
        self.ovelha = ovelha
        self.repolho = repolho
        self.estado_pai = estado_pai

    # Um estado é valido se a ovelha não está sozinha com o lobo ou
    # com o repolho
    def is_valid(self):
        if (self.lobo == self.ovelha) and (self.lobo != self.fazendeiro):
            return False
        if (self.ovelha == self.repolho) and (self.ovelha != self.fazendeiro):
            return False
        return True

    #gera os proximos estados com base nas açoes possíveis 
    def gen_next(self):
        filhos = []
        operacoes = []

        if (self.fazendeiro == 'e'):
            # vai
            operacoes += [('d', self.lobo, self.ovelha, self.repolho)]
        if (self.fazendeiro == 'e' and self.lobo == 'e'):
            # leva lobo
            operacoes += [('d', 'd', self.ovelha, self.repolho)]
        if (self.fazendeiro == 'e' and self.ovelha == 'e'):
            # leva ovelha
            operacoes += [('d', self.lobo, 'd', self.repolho)]
        if (self.fazendeiro == 'e' and self.repolho == 'e'):
            # leva repolho
            operacoes += [('d', self.lobo, self.ovelha, 'd')]
        
        if (self.fazendeiro == 'd'):
            # volta
            operacoes += [('e', self.lobo, self.ovelha, self.repolho)]
        if (self.fazendeiro == 'd' and self.lobo == 'd'):
            # volta com lobo
            operacoes += [('e', 'e', self.ovelha, self.repolho)]
        if (self.fazendeiro == 'd' and self.ovelha == 'd'):
            # volta com ovelha
            operacoes += [('e', self.lobo, 'e', self.repolho)]
        if (self.fazendeiro == 'd' and self.repolho == 'd'):
            # volta com repolho
            operacoes += [('e', self.lobo, self.ovelha, 'e')]

        for operacao in operacoes:
            novo_filho = Estado(operacao[0], operacao[1], operacao[2], operacao[3], self)
            if novo_filho.is_valid():
                filhos.append(novo_filho)

        return filhos
    
    def get_path(self):
        caminho = [self]

        e = self.estado_pai
        while e != None:
            caminho.append(e)
            e = e.estado_pai
        
        return caminho

    # o objetivo é o estado em que todos estão no lado direito do rio
    def is_goal(self):
        return self.fazendeiro == self.lobo == self.ovelha == self.repolho == 'd'
    
    def __str__(self):
        return f"[{self.fazendeiro}, {self.lobo}, {self.ovelha}, {self.repolho}]"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Estado) and (self.fazendeiro == other.fazendeiro \
            and self.lobo == other.lobo \
            and self.ovelha == other.ovelha \
            and self.repolho == other.repolho
        )

# Faz a busca em PROFUNDIDADE do problema.
# É mantida uma fila de estados a ser abertos, bem como uma fila de estados fechados.
# O estado no início da fila é aberto primeiro, removido da fila e adicionado ao final 
# da lista de estados fechados.
# Os estados filhos válidos são adicionados ao INÍCIO da fila, se já não estiverem 
# enfileirados
def busca_profundidade(estado_inicial):
    fila = []
    fila.append(estado_inicial)
    fechados = []

    while fila:
        print("\nFila: ", fila)
        print("\nFechados: ", fechados, "\n")
        e = fila.pop(0)
        fechados.append(e)

        print("Abrindo Estado: ", e, "\n")

        if e.is_goal():
            print("Objetivo encontrado!\n")
            return e.get_path()[::-1]
        
        print("Gerando estados filhos: ")
        for next in e.gen_next():
            if next not in fila and next not in fechados:
                print(f"\tEnfileirando estado: {next}")
                fila.insert(0, next)
            else:
                print(f"\t{next} já está na fila: ")
        print("\n-----")
        print("-----")
    else:
        return None

def imprimir_caminho(caminho):
    for i, estado in enumerate(caminho):
        print(f"Passo {i + 1}:")
        print(f"Posição do Fazendeiro: {'Esquerda' if estado.fazendeiro == 'e' else 'Direita'}")
        print(f"Posição do Lobo: {'Esquerda' if estado.lobo == 'e' else 'Direita'}")
        print(f"Posição da Ovelha: {'Esquerda' if estado.ovelha == 'e' else 'Direita'}")
        print(f"Posição do Repolho: {'Esquerda' if estado.repolho == 'e' else 'Direita'}")
        print("")

estado_inicial = Estado('e', 'e', 'e', 'e', None)

caminho = busca_profundidade()

if caminho:
    print("Caminho para solução:")
    imprimir_caminho(caminho)
else:
    print("Não há solução possível.")
