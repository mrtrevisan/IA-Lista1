import math

# Classe que representa um nó da árvore
# Guarda o numero de palitos restantes e de quem é o turno
# Rodada_max -> true se a é a vez do jogador Max
# -> false se é a vez do jogador Min
class Node:
    def __init__(self, palitos_restantes, rodada_max):
        self.palitos_restantes = palitos_restantes
        self.rodada_max = rodada_max

    # gera os estados filhos com base nas jogadas possíveis:
    # Retirar 1, 2 ou 3 palitos
    def gen_next(self):
        filhos = []
        for move in range(1, 4):  
            if self.palitos_restantes - move >= 0:
                filhos.append(Node(self.palitos_restantes - move, not self.rodada_max))
        return filhos

    def folha(self):
        return self.palitos_restantes == 0

    # quem enfileira um estado com 0 palitos, perde
    # se é a vez do jogador Max, e há 0 palitos, foi o Min quem jogou errado
    def valor(self):
        if self.rodada_max:
            return 1
        else:
            return -1
        
    def __str__(self):
        return f"[Palitos: {self.palitos_restantes}, Turno: {'Max' if self.rodada_max else 'Min'}]"

    def __repr__(self):
        return str(self)

# Função para resolver o jogo usando minimax com poda alfa-beta
def minimax(node, alfa, beta):
    if node.folha():
        return node.valor()

    if node.rodada_max:
        print("\nRodada do Max")
        max_val = -math.inf

        for filho in node.gen_next():
            print(f"\n\tExpandido estado {filho}")
            val = minimax(filho, alfa, beta)

            print(f"\tComparando {val} com {max_val}")
            max_val = max(max_val, val)

            alfa = max(alfa, val)
            print(f"\tAlfa agora é {alfa}")

            if beta <= alfa:
                print("\t\tPoda\n")
                break

        print("")
        return max_val
    else:
        print("\nRodada do Min")
        min_val = math.inf

        for filho in node.gen_next():
            print(f"\n\tExpandido estado {filho}")
            val = minimax(filho, alfa, beta)

            print(f"\tComparando {val} com {min_val}")
            min_val = min(min_val, val)
            
            beta = min(beta, val)
            print(f"\tBeta agora é {beta}")

            if beta <= alfa:
                print("\t\tPoda\n")
                break

        print("")
        return min_val

root = Node(5, True)
resultado = minimax(root, -math.inf, math.inf)
print("Max pode ganhar!" if resultado == 1 else "Max não pode ganhar.")
