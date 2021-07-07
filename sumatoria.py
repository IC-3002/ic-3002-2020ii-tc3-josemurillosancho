def sumatoria_cubica(n):
	"""Funcion para calcular una sumatoria cubica
	E: Un numero entero positivo
	S: Un numero entero positivo 
	R: Ocupa ser un numero positivo"""
	resultado = 0
	for i in range(1,n+1):
		for j in range(1,i+1):
			for k in range(j, i+j+1):
				resultado = resultado + 1
	return resultado

def sumatoria_constante(n):
	"""Funcion para calcular una sumatoria de manera constante 
	E: Un numero entero positivo
	S: Un numero entero positivo 
	R: Ocupa ser un numero positivo"""
	resultado = (n*(n+1)*(n+2))/3
	return resultado

