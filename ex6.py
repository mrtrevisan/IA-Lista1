rotas = [
    ('a', 'b', 7), 
    ('a', 'c', 9), 
    ('a', 'd', 3), 
    ('b', 'f', 3), 
    ('b', 'i', 4),
    ('c', 'j', 5), 
    ('d', 'e', 1), 
    ('f', 'g', 2), 
    ('g', 'h', 3),
    ('i', 'k', 5),
    ('j', 'l', 6),
    ('l', 'k', 4)
]

heuristica = {
    'a': 15, 'b': 7, 'c': 6, 'd': 14, 'e': 15,
    'f': 7, 'g': 8, 'h': 5, 'i': 5, 'j': 3,
    'k': 0, 'l': 4
}

def h(cidade):
    return heuristica[cidade]

def busca_gulosa(origem, destino):
    caminho = []

    cidade_atual = origem
    while cidade_atual != destino:
        print("Cidade Atual: ", cidade_atual, "\n")            
        print("Procurando novos destinos: ")

        opcoes = []
        for (cidade_origem, cidade_destino, _) in rotas:
            if (cidade_origem == cidade_atual):
                print(f"\tEncontrada rota de {cidade_origem} até {cidade_destino}")

                if (cidade_destino not in caminho):
                    print(f"\t\tRota adicionada às possibilidades: {cidade_origem, cidade_destino, h(cidade_destino)}")
                    opcoes.append((cidade_origem, cidade_destino, h(cidade_destino)))
                else:
                    print(f"\t\tCidade {cidade_destino} já foi visitada")

        if (not opcoes):
            print("Chegou em um beco sem saída, fim do algoritmo.")
            return None, 0
        
        print("\n\tPossíveis caminhos: ", opcoes)

        melhor_escolha = min(opcoes, key = lambda t: t[2])
        print("\tMelhor escolha: ", melhor_escolha, '\n')

        caminho += [cidade_atual]
        cidade_atual = melhor_escolha[1]
    else:
        print("Objetivo encontrado!\n")
        return caminho + [cidade_atual]

# Execução
origem = 'a'
destino = 'k'
caminho = busca_gulosa(origem, destino)

if caminho:
    print(f"Existe caminho de {origem} para {destino}.")
    print(f"{' -> '.join(caminho)}")

else:
    print(f"Não existe caminho de {origem} para {destino}.")
