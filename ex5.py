class Estado:
    def __init__(self, cidade, caminho, custo_acumulado):
        self.cidade = cidade
        self.caminho = caminho
        self.custo_acumulado = custo_acumulado

    def __str__(self):
        return f"[{self.cidade}, {self.caminho}, {self.custo_acumulado}]"

    def __repr__(self):
        return str(self)

class Voo:
    def __init__(self, origem, destino, custo):
        self.origem = origem
        self.destino = destino
        self.custo = custo
    
    def __str__(self):
        return f"[{self.origem}, {self.destino}, {self.custo}]"

    def __repr__(self):
        return str(self)

voos = [
    Voo('a', 'b', 1), 
    Voo('a', 'c', 9), 
    Voo('a', 'd', 4), 
    Voo('b', 'c', 7), 
    Voo('b', 'e', 6),
    Voo('b', 'f', 1),
    Voo('c', 'f', 7), 
    Voo('d', 'f', 4), 
    Voo('d', 'g', 5), 
    Voo('e', 'h', 9), 
    Voo('f', 'h', 4),
    Voo('g', 'h', 1)
]

def busca_melhor_escolha(origem, destino):
    fila = []
    fila.append(Estado(origem, [], 0))
    fechados = []

    while fila:
        print("\nFila: ", fila)
        print("\nFechados: ", fechados, "\n")
        e = fila.pop(0)
        fechados.append(e)

        print("Melhor escolha: ", e, "\n")
        if (e.cidade == destino):
            return e.caminho + [e.cidade], e.custo_acumulado
    

        for voo in voos:
            if voo.origem == e.cidade and voo.destino not in e.caminho:
                novo_estado = Estado(
                    voo.destino, 
                    e.caminho + [e.cidade], 
                    e.custo_acumulado + voo.custo
                )
                fila.append(novo_estado)

        fila.sort(key=lambda e: e.custo_acumulado)
        
    else:
        print("Objetivo Inalcançável\n")
        return None
    
origem = 'a'
destino = 'h'
caminho, custo = busca_melhor_escolha(origem, destino)

if caminho:
    print(f"Caminho encontrado de {origem} para {destino}!")
    print(f"{' -> '.join(caminho)}")
    print(f"Custo total: ", custo)
else:
    print(f"Não há caminho possível")
