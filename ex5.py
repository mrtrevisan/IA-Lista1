voos = [
    ('a', 'b', 1), 
    ('a', 'c', 9), 
    ('a', 'd', 4), 
    ('b', 'c', 7), 
    ('b', 'e', 6),
    ('b', 'f', 1),
    ('c', 'f', 7), 
    ('d', 'f', 4), 
    ('d', 'g', 5), 
    ('e', 'h', 9), 
    ('f', 'h', 4),
    ('g', 'h', 1)
]

def busca_melhor_escolha(origem, destino):
    caminho = []
    custo_total = 0

    cidade_atual = origem
    while cidade_atual != destino:
        print("Cidade Atual: ", cidade_atual, "\n")            
        print("Procurando novos destinos: ")

        opcoes = []
        for (cidade_origem, cidade_destino, custo) in voos:
            if (cidade_origem == cidade_atual):
                print(f"\tEncontrado voo de {cidade_origem} até {cidade_destino}")

                if (cidade_destino not in caminho):
                    print(f"\t\tVoo adicionado às possibilidades: {cidade_origem, cidade_destino, custo}")
                    opcoes.append((cidade_origem, cidade_destino, custo))
                else:
                    print(f"\t\tCidade {cidade_destino} já foi visitada")

        if (not opcoes):
            print("Chegou em um beco sem saída, fim do algoritmo.")
            return None, 0
        
        print("\n\tPossíveis caminhos: ", opcoes)

        melhor_escolha = min(opcoes, key = lambda t: t[2])
        print("\tMelhor escolha: ", melhor_escolha, '\n')

        caminho += [cidade_atual]
        custo_total += melhor_escolha[2]
        cidade_atual = melhor_escolha[1]
    else:
        print("Objetivo encontrado!\n")
        return caminho + [cidade_atual], custo_total
    
origem = 'a'
destino = 'h'
caminho, custo = busca_melhor_escolha(origem, destino)

if caminho:
    print(f"Caminho encontrado de {origem} para {destino}!")
    print(f"{' -> '.join(caminho)}")
    print(f"Custo total: ", custo)
else:
    print(f"Não há caminho possível")
