# 	1. Escreva uma funcao que recebe como entrada as dimensoes M e N e o elemento E de preenchimento
# 	e retorna uma lista de listas que corresponde a uma matriz MxN contendo o elemento e em todas
#	as posicoes. Exemplo:
#		>>> cria_matriz(2, 3, 0)
#		[[0, 0, 0], [0, 0, 0]]

def f_preencheMatriz(m, n, el):
	matrizPreenchida = []
	
	for lin in range(m):
		matrizPreenchida.append([])
		for col in range(n):
			matrizPreenchida[lin].append(el)
		#fim for
	#fim for
		
	return matrizPreenchida
#fim funcao

def main():
	m, n, el, matriz = 0, 0, 0, [][]
	
	m = int(input("Informe a qtd de linhas da matriz: "))
	n = int(input("Informe a qtd de colunas da matriz: "))
	m = int(input("Informe o elemento a ser preenchido nas posicoes da matriz: "))
	
	matriz = f_preencheMatriz(m, n, el)
	
	print(matriz)
#fim main

if __name__ == '__main__':
	main()
#fim if
