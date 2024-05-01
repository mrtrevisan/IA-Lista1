voos = {
    1: ('a', 'b'), 
    2: ('a', 'b'), 
    3: ('a', 'd'), 
    4: ('b', 'e'), 
    5: ('b', 'f'),
    6: ('c', 'g'),
    7: ('c', 'h'), 
    8: ('c', 'i'), 
    9: ('d', 'j'), 
    10: ('e', 'k'),
    11: ('e', 'l'), 
    12: ('g', 'm'), 
    13: ('j', 'n'), 
    14: ('j', 'o'), 
    15: ('k', 'f'),
    16: ('l', 'h'), 
    17: ('m', 'd'), 
    18: ('o', 'a'), 
    19: ('n', 'b')
}

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
        for _, (cidade_origem, cidade_destino) in voos.items():
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
