import math

MAX, MIN = math.inf, -1*math.inf
P_MAX = 4

# Aplica o algoritmo Minimax
# A árvore de busca está abstraída como um array
# A iteração sobre esse array é feita recursivamente e
# de maneira a simular uma navegação em árvore 
def minimax(profund, index, max_player, valores, alfa, beta): 
	print(f"\nProfundidade: {profund}")
	
	if profund == P_MAX: 
		return valores[index] 


	if max_player: 
		melhor = MIN
		print("\tRodada do Max")

		for i in range(0, 2): 
			print(f"\t\tAlfa: {alfa} \n\t\tBeta: {beta}")
			val = minimax(profund + 1, index * 2 + i, False, valores, alfa, beta)

			print(f"\t\tComparando {val} com {melhor}")
			melhor = max(melhor, val) 
			alfa = max(alfa, melhor) 

			print(f"\t\tAlfa agora é {alfa}")
			if alfa >= beta: 
				print("\t\tPoda\n")
				break

			print("")	

			
	else:
		melhor = MAX
		print("\tRodada do Min")

		for i in range(0, 2): 
			print(f"\t\tAlfa: {alfa} \n\t\tBeta: {beta}")
		
			val = minimax(profund + 1, index * 2 + i, True, valores, alfa, beta)
			
			print(f"\t\tComparando {val} com {melhor}")
			melhor = min(melhor, val) 
			beta = min(beta, melhor) 

			print(f"\t\tBeta agora é {alfa}")
			if alfa >= beta:
				print("\t\tPoda\n")
				break
			
			print("")	

	return melhor 
	
if __name__ == "__main__": 

	valores = [20, 33, -45, 31, 24, 25, -10, 20, 40, -25, 18, -42, 24, -19, 36, -41] 
	print("O melhor valor é :", minimax(0, 0, True, valores, MIN, MAX)) 