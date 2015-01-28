# 	2. Faca uma func˜ao que recebe uma matriz e a exibe na tela no formato usual utilizado na matematica

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

def f_imprimeMatriz(mat):
	for lin in mat:
		for el in lin:
			print('%d ' %(el), end="");
		#fim for
		print()
	#fim for
#fim funcao

def main():
	m, n, el, matriz = 0, 0, 0, []
	
	m = int(input("Informe a qtd de linhas da matriz: "))
	n = int(input("Informe a qtd de colunas da matriz: "))
	el = int(input("Informe o elemento a ser preenchido nas posicoes da matriz: "))
	
	matriz = f_preencheMatriz(m, n, el)
	f_imprimeMatriz(matriz)
	
#fim main

if __name__ == '__main__':
	main()
#fim if
