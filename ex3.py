class Estado:
    def __init__(self, fazendeiro, lobo, ovelha, repolho, estado_pai):
        self.fazendeiro = fazendeiro
        self.lobo = lobo
        self.ovelha = ovelha
        self.repolho = repolho
        self.estado_pai = estado_pai

    def is_valid(self):
        if (self.lobo == self.ovelha) and (self.lobo != self.fazendeiro):
            return False
        if (self.ovelha == self.repolho) and (self.ovelha != self.fazendeiro):
            return False
        return True

    def gen_next(self):
        filhos = []
        operacoes = []

        if (self.fazendeiro == 'e'):
            operacoes += [('d', self.lobo, self.ovelha, self.repolho)]
        if (self.fazendeiro == 'e' and self.lobo == 'e'):
            operacoes += [('d', 'd', self.ovelha, self.repolho)]
        if (self.fazendeiro == 'e' and self.ovelha == 'e'):
            operacoes += [('d', self.lobo, 'd', self.repolho)]
        if (self.fazendeiro == 'e' and self.repolho == 'e'):
            operacoes += [('d', self.lobo, self.ovelha, 'd')]
        
        if (self.fazendeiro == 'd'):
            operacoes += [('e', self.lobo, self.ovelha, self.repolho)]
        if (self.fazendeiro == 'd' and self.lobo == 'd'):
            operacoes += [('e', 'e', self.ovelha, self.repolho)]
        if (self.fazendeiro == 'd' and self.ovelha == 'd'):
            operacoes += [('e', self.lobo, 'e', self.repolho)]
        if (self.fazendeiro == 'd' and self.repolho == 'd'):
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

# Função para buscar a solução usando busca em largura
def busca_largura():
    estado_inicial = Estado('e', 'e', 'e', 'e', None)
    fila = []
    fila.append(estado_inicial)

    for e in fila:
        print("\nFila: ", fila, "\n")

        print("Abrindo Estado: ", e, "\n")

        if e.is_goal():
            print("Objetivo encontrado!\n")
            return e.get_path()[::-1]
        
        print("Gerando estados filhos: ")
        for next in e.gen_next():
            if next not in fila:
                print(f"\tEnfileirando estado: {next}")
                fila.append(next)
            else:
                print(f"\t{next} já está na fila: ")
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

caminho = busca_largura()
if caminho:
    print("Caminho para solução:")
    imprimir_caminho(caminho)
else:
    print("Não há solução possível.")
