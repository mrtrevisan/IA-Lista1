class Estado:
    def __init__(self, jarro1, jarro2, estado_pai):
        self.jarro1 = jarro1
        self.jarro2 = jarro2
        self.estado_pai = estado_pai

    def is_valid(self):
        return self.jarro1 >= 0 and self.jarro1 <= 3 and self.jarro2 >= 0 and self.jarro2 <= 4

    def gen_next(self):
        filhos = []
        operacoes = []

        if (self.jarro1 < 3):
            operacoes += [(3, self.jarro2)]

        if (self.jarro2 < 4):
            operacoes += [(self.jarro1, 4)]

        if (self.jarro1 > 0):
            operacoes += [(0, self.jarro2)]

        if (self.jarro2 > 0):
            operacoes += [(self.jarro1, 0)]

        if (self.jarro1 > 0) and (self.jarro2 < 4) and (self.jarro1 + self.jarro2 <= 4):
            operacoes += [(0, self.jarro1 + self.jarro2)]

        if (self.jarro1 > 0) and (self.jarro2 < 4) and (self.jarro1 + self.jarro2 > 4):
            operacoes += [(self.jarro1 + self.jarro2 -4, 4)]

        if (self.jarro1 < 3) and (self.jarro2 > 0) and (self.jarro1 + self.jarro2 <= 3):
            operacoes += [(self.jarro1 + self.jarro2, 0)]

        if (self.jarro1 < 3) and (self.jarro2 > 0) and (self.jarro1 + self.jarro2 > 3):
            operacoes += [(3, self.jarro1 + self.jarro2 -3)]
        
        for operacao in operacoes:
            novo_filho = Estado(operacao[0], operacao[1], self)
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
        return self.jarro2 == 2
    
    def __str__(self):
        return f"[{self.jarro1}, {self.jarro2}]"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Estado) and (self.jarro1 == other.jarro1 \
            and self.jarro2 == other.jarro2 
        )

# Função para buscar a solução usando busca em largura
def busca_largura():
    estado_inicial = Estado(0, 0, None)
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
        print(f"Volume de líquido no jarro 1: {estado.jarro1}")
        print(f"Volume de líquido no jarro 2: {estado.jarro2}")
        print("")

caminho = busca_largura()
if caminho:
    print("Caminho para solução:")
    imprimir_caminho(caminho)
else:
    print("Não há solução possível.")
