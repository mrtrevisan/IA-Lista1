N_CAN = 3
N_MIS = 3

class Estado:
    def __init__(self,
                 missionarios_esquerda, canibais_esquerda,
                 missionarios_direita, canibais_direita,
                 barco_esquerda,
                 estado_pai
                ):
        self.missionarios_esquerda = missionarios_esquerda
        self.canibais_esquerda = canibais_esquerda
        self.missionarios_direita = missionarios_direita
        self.canibais_direita = canibais_direita
        self.barco_esquerda = barco_esquerda
        self.estado_pai = estado_pai

    def __eq__(self, other):
        return isinstance(other, Estado) and (self.missionarios_esquerda == other.missionarios_esquerda \
            and self.canibais_esquerda == other.canibais_esquerda \
            and self.missionarios_direita == other.missionarios_direita \
            and self.canibais_direita == other.canibais_direita \
            and self.barco_esquerda == other.barco_esquerda
        )


    def is_valid(self):
        if (self.canibais_esquerda < 0) or \
           (self.canibais_direita < 0) or \
           (self.missionarios_esquerda < 0) or \
           (self.missionarios_direita < 0):
            return False
        if (self.canibais_esquerda > self.missionarios_esquerda > 0) or \
           (self.canibais_direita > self.missionarios_direita > 0):
            return False
        return True

    def generate_next(self):
        filhos = []
        movimentos = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

        for movimento in movimentos:
            if (self.barco_esquerda):
                novo_estado = Estado(self.missionarios_esquerda - movimento[0], 
                    self.canibais_esquerda - movimento[1],
                    self.missionarios_direita + movimento[0],
                    self.canibais_direita + movimento[1],
                    0,
                    self
                )
            else:
                novo_estado = Estado(self.missionarios_esquerda + movimento[0], 
                    self.canibais_esquerda + movimento[1],
                    self.missionarios_direita - movimento[0],
                    self.canibais_direita - movimento[1],
                    1,
                    self
                )
            if novo_estado.is_valid():
                filhos.append(novo_estado)
                
        return filhos

    def is_goal(self):
        return self.missionarios_esquerda == 0 and self.canibais_esquerda == 0 and \
               self.missionarios_direita == N_MIS and self.canibais_direita == N_CAN
    
    def get_path(self):
        caminho = [self]

        e = self.estado_pai
        while e != None:
            caminho.append(e)
            e = e.estado_pai
        
        return caminho
    
    def __str__(self):
        return f"[{self.missionarios_esquerda}, {self.canibais_esquerda}, {self.missionarios_direita}, {self.canibais_direita}, {'Esquerda' if self.barco_esquerda else 'Direita'}]"

    def __repr__(self):
        return str(self)
    
def busca_largura():
    estado_inicial = Estado(N_MIS, N_CAN, 0, 0, 1, None)
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
        for next in e.generate_next():
            if next not in fila and next not in fechados:
                print(f"\tEnfileirando estado: {next}")
                fila.append(next)
            else:
                print(f"\t{next} já está na fila: ")
        print("\n-----")
        print("-----")
    else:
        return None


def imprimir_caminho(caminho):
    for i, estado in enumerate(caminho):
        print(f"Passo {i + 1}:")
        print(f"Missionários na margem esquerda: {estado.missionarios_esquerda}")
        print(f"Canibais na margem esquerda: {estado.canibais_esquerda}")
        print(f"Missionários na margem direita: {estado.missionarios_direita}")
        print(f"Canibais na margem direita: {estado.canibais_direita}")
        print(f"Posição do barco: {'Esquerda' if estado.barco_esquerda else 'Direita'}")
        print("")

caminho = busca_largura()
if caminho:
    print("Caminho para solução:")
    imprimir_caminho(caminho)
else:
    print("Não há solução possível.")