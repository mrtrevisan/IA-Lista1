#lista de voos entre cidades (origem, destino)
voos = [
    ('a', 'b'), ('a', 'b'), ('a', 'd'), ('b', 'e'), 
    ('b', 'f'), ('c', 'g'), ('c', 'h'), ('c', 'i'), 
    ('d', 'j'), ('e', 'k'), ('e', 'l'), ('g', 'm'), 
    ('j', 'n'), ('j', 'o'), ('k', 'f'), ('l', 'h'), 
    ('m', 'd'), ('o', 'a'), ('n', 'b')
]

# Faz a busca em LARGURA ou PROFUNDIDADE do problema.
# É mantida uma fila de estados a ser abertos, bem como uma fila de estados fechados.
# O estado no início da fila é aberto primeiro, removido da fila e adicionado ao final 
# da lista de estados fechados.
# Os estados filhos válidos são adicionados ao INÍCIO ou FINAL da fila 
# (a depender do modo de busca), se já não estiverem enfileirados

# Um estado é representado por uma tupla (cidade, caminho)
def busca(modo, origem, destino):
    fila = []
    fila.append((origem, []))
    fechados = []

    while fila:
        print("\nFila: ", fila)
        print("\nFechados: ", fechados, "\n")

        c, caminho = fila.pop(0)
        fechados.append((c, caminho))

        print("Cidade Atual: ", c, "\n")

        if c == destino:
            print("Objetivo encontrado!\n")
            return caminho + [c]
        
        print("Procurando novos destinos: ")
        for (cidade_origem, cidade_destino) in voos:
            if (cidade_origem == c):
                print(f"\tEncontrado voo de {cidade_origem} até {cidade_destino}")

                if (cidade_destino not in caminho and cidade_destino not in [t[0] for t in fila + fechados]):
                    print(f"\t\tEnfileirando cidade: {cidade_destino}")
                    if modo == 'largura':
                        fila.append((cidade_destino, caminho + [c]))
                    if modo == 'profundidade':
                        fila.insert(0, (cidade_destino, caminho + [c]))
                else:
                    print(f"\t\tCidade {cidade_destino} já foi visitada ou já está na fila.")
        print("\n-----")
        print("-----")
    else:
        return None
    
origem = 'a'
destino = 'j'

print("Pela busca em largura: ")
caminho = busca('largura', origem, destino)

if caminho:
    print(f"Caminho encontrado de {origem} para {destino}!")
    print(f"{' -> '.join(caminho)}")
else:
    print(f"Não há caminho possível")

print("\n========================================================================================================\n")

print("Pela busca em profundidade: ")
caminho = busca('profundidade', origem, destino)

if caminho:
    print(f"Caminho encontrado de {origem} para {destino}!")
    print(f"{' -> '.join(caminho)}")
else:
    print(f"Não há caminho possível")
