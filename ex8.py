def find_b(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'b':
                return (i, j)


def h(state, custo):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != objetivo[i][j] and state[i][j] != 'b':
                count += 1
    return count + custo

def gen_next(state):
    next = []
    b_row, b_col = find_b(state)

    # Movimento para cima
    if b_row > 0:
        new_state = [row[:] for row in state]
        new_state[b_row][b_col], new_state[b_row - 1][b_col] = new_state[b_row - 1][b_col], new_state[b_row][b_col]
        next.append(new_state)

    # Movimento para baixo
    if b_row < 2:
        new_state = [row[:] for row in state]
        new_state[b_row][b_col], new_state[b_row + 1][b_col] = new_state[b_row + 1][b_col], new_state[b_row][b_col]
        next.append(new_state)

    # Movimento para a esquerda
    if b_col > 0:
        new_state = [row[:] for row in state]
        new_state[b_row][b_col], new_state[b_row][b_col - 1] = new_state[b_row][b_col - 1], new_state[b_row][b_col]
        next.append(new_state)

    # Movimento para a direita
    if b_col < 2:
        new_state = [row[:] for row in state]
        new_state[b_row][b_col], new_state[b_row][b_col + 1] = new_state[b_row][b_col + 1], new_state[b_row][b_col]
        next.append(new_state)

    return next

# Algoritmo A*
def a_star(estado_inicial):
    fila = [(estado_inicial, 0, h(estado_inicial, 0))]
    fechados = []

    while fila:
        print("\nFila: ", fila)
        print("\nFechados: ", fechados, "\n")
        e, custo, heur = fila.pop(0)
        fechados.append((e, custo, heur))

        print("\tMelhor escolha: ", e, " Heurística: ", heur, "\n")

        if (e == objetivo):
            return e
        
        for next in gen_next(e):
            if next not in [t[0] for t in fechados + fila]:
                fila.append((next, custo+1, h(next, custo+1)))
                print(f"\t\t{next} adicionado à fila")

        fila.sort(key=lambda t : t[2])

    return None

# Algoritmo Melhor Escolha com heuristica

def melhor_esc_heur(estado_inicial):
    fila = [(estado_inicial, h(estado_inicial, 0))]
    fechados = []

    while fila:
        print("\nFila: ", fila)
        print("\nFechados: ", fechados, "\n")
        e, heur = fila.pop(0)
        fechados.append((e, heur))

        print("\tMelhor escolha: ", e, " Heurística: ", heur, "\n")

        if (e == objetivo):
            return e
        
        for next in gen_next(e):
            if next not in [t[0] for t in fechados + fila]:
                fila.append((next, h(next, 0)))
                print(f"\t\t{next} adicionado à fila")

        fila.sort(key=lambda t : t[1])

    return None

# Algoritmo Melhor Escolha
def melhor_escolha(estado_inicial):
    fila = [(estado_inicial, 0)]
    fechados = []

    while fila:
        print("\nFila: ", fila)
        print("\nFechados: ", fechados, "\n")
        e, custo = fila.pop(0)
        fechados.append((e, custo))

        print("\tMelhor escolha: ", e, " Custo: ", custo, "\n")

        if (e == objetivo):
            return e
        
        for next in gen_next(e):
            if next not in [t[0] for t in fechados + fila]:
                fila.append((next, custo+1))
                print(f"\t\t{next} adicionado à fila")

        fila.sort(key=lambda t : t[1])

    return None

# Estado inicial
inicial = [
    [  1, 2, 3],
    ['b', 6, 4],
    [  8, 7, 5]
]

# Estado final
objetivo = [
    [1,  2,  3],
    [8, 'b', 4], 
    [7,  6,  5]
]

print("Pelo algoritmo A*: ")

# Algoritmo A*
solution = a_star(inicial)
if solution:
    print("Solução encontrada:")
    for row in solution:
        print(row)
else:
    print("Não foi encontrada uma solução.")

print("\n========================================================================================================\n")

print("Pelo algoritmo Melhor Escolha: ")

# Melhor escolha
solution = melhor_escolha(inicial)
if solution:
    print("Solução encontrada:")
    for row in solution:
        print(row)
else:
    print("Não foi encontrada uma solução.")

print("\n========================================================================================================\n")

print("Pelo algoritmo Melhor Escolha com heurística: ")

# Melhor escolha heuristica
solution = melhor_esc_heur(inicial)
if solution:
    print("Solução encontrada:")
    for row in solution:
        print(row)
else:
    print("Não foi encontrada uma solução.")
