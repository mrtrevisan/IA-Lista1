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

def busca_largura(origem, destino):
    fila = []
    fila.append((origem, []))

    for c, caminho in fila:
        print("\nFila: ", fila, "\n")

        print("Cidade Atual: ", c, "\n")

        if c == destino:
            print("Objetivo encontrado!\n")
            return caminho + [c]
        
        print("Procurando novos destinos: ")
        for num, (cidade_origem, cidade_destino) in voos.items():
            if (cidade_origem == c):
                print(f"\tEncontrado voo de {cidade_origem} até {cidade_destino}")

                if (cidade_destino not in caminho and cidade_destino not in [tupla[0] for tupla in fila]):
                    print(f"\t\tEnfileirando cidade: {cidade_destino}")
                    fila.append((cidade_destino, caminho + [c]))
                else:
                    print(f"\t\tCidade {cidade_destino} já foi visitada ou já está na fila.")
    else:
        return None
    
origem = 'a'
destino = 'j'
caminho = busca_largura(origem, destino)

if caminho:
    print(f"Caminho encontrado de {origem} para {destino}!")
    print(f"{' -> '.join(caminho)}")
else:
    print(f"Não há caminho possível")