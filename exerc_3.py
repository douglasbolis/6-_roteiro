#	3. Crie uma func˜ao que recebe como entrada uma lista de listas e verifica se a entrada corresponde
#	a uma matriz. Uma lista de listas so e uma matriz quando todas as listas internas possuırem o
#	mesmo tamanho.

def f_verificaMatriz(mat):
	ehMatriz, tam = False, 0
	
	tam = len(mat[0])
	
	for lin in range(len(mat)):
		if (tam == len(mat[lin])):
			ehMatriz = True
		else:
			ehMatriz = False
		#fim if
	#fim for
	return ehMatriz
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
	matriz = [[2], [1, 3], [3, 9, 1], [1, 3, 7, 1]]
	ehMatriz = f_verificaMatriz(matriz)
	
	print("a lista de listas\n")
	f_imprimeMatriz(matriz)
	
	if (ehMatriz):
		print("\neh uma matriz")
	else:
		print("\nnao eh uma matriz")
	#fim if
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
