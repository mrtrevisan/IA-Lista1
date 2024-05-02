class Estado:
    # Construtor da classe Estado 
    # Os atributos representam a cidade, o caminho percorrido até ela 
    # bem como o custo acumulado para chegar até ela pelo caminho escolhido
    def __init__(self, cidade, caminho, custo_acumulado):
        self.cidade = cidade
        self.caminho = caminho
        self.custo_acumulado = custo_acumulado

    def __str__(self):
        return f"[{self.cidade}, {self.caminho}, {self.custo_acumulado}]"

    def __repr__(self):
        return str(self)

class Rota:
    # Construtor da classe Rota 
    # Os atributos representam a cidade origem, destino e o custo da rota
    def __init__(self, origem, destino, custo):
        self.origem = origem
        self.destino = destino
        self.custo = custo
    
    def __str__(self):
        return f"[{self.origem}, {self.destino}, {self.custo}]"

    def __repr__(self):
        return str(self)

# Lista de rotas possíveis: (origem, destino, custo)
rotas = [
    Rota('a', 'b', 7), 
    Rota('a', 'c', 9), 
    Rota('a', 'd', 3), 
    Rota('b', 'f', 3), 
    Rota('b', 'i', 4),
    Rota('c', 'j', 5), 
    Rota('d', 'e', 1), 
    Rota('f', 'g', 2), 
    Rota('g', 'h', 3),
    Rota('i', 'k', 5),
    Rota('j', 'l', 6),
    Rota('l', 'k', 4)
]

# heuristica que representa a distância em linha reta até a cidade k
heuristica = {
    'a': 15, 'b': 7, 'c': 6, 'd': 14, 'e': 15,
    'f': 7, 'g': 8, 'h': 5, 'i': 5, 'j': 3,
    'k': 0, 'l': 4
}

# A função heurística considera a soma entre:
# dist. em linha reta entre a cidade destino e a cidade objetivo
# o custo da rota até cidade destino
def h(x, c):
    return heuristica[x] + c

# Faz a busca usando o algoritmo A*.
# É mantida uma fila de estados a ser abertos, bem como uma fila de estados fechados.
# O estado no início da fila é aberto primeiro, removido da fila e adicionado ao final 
# da lista de estados fechados.
# Os estados filhos válidos são adicionados ao FINAL da fila.
# A fila é então ORDENADA por ordem de melhor heurística.
# É usada a função heurística
def busca_a_estrela(origem, destino):
    fila = []
    fila.append((Estado(origem, [], 0), h(origem, 0)))
    fechados = []

    while fila:
        print("\nFila: ", fila)
        print("\nFechados: ", fechados, "\n")
        e, heur = fila.pop(0)
        fechados.append((e, heur))

        print("Melhor escolha: ", e, " Heurística: ", heur, "\n")
        if (e.cidade == destino):
            return e.caminho + [e.cidade], e.custo_acumulado
    

        for r in rotas:
            if r.origem == e.cidade and r.destino not in e.caminho:
                novo_estado = Estado(
                    r.destino, 
                    e.caminho + [e.cidade],
                    e.custo_acumulado + r.custo
                )
                fila.append((novo_estado, h(r.destino, novo_estado.custo_acumulado)))

        fila.sort(key=lambda t : t[1])
    else:
        print("Objetivo Inalcançável\n")
        return None

# Execução
origem = 'a'
destino = 'k'
caminho, custo = busca_a_estrela(origem, destino)

if caminho:
    print(f"Caminho encontrado de {origem} para {destino}.")
    print(f"{' -> '.join(caminho)}")
    print(f"Custo: {custo}")

else:
    print(f"Não existe caminho de {origem} para {destino}.")
