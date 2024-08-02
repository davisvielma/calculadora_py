def sumar(a: float, b: float) -> float:
	return a + b

def restar(a: float, b: float) -> float:
	return a - b

def multiplicar(a: float, b: float) -> float:
	return a * b

def dividir(a: float, b: float) -> float:
	if b == 0:
		raise ValueError('El denominador no puede ser igual a 0')

	return a / b